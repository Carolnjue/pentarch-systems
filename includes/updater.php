<?php
/**
 * Update the plugin from its GitHub repository, then optionally re-run set-up.
 */
if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

define( 'PSS_REPO_ZIP', 'https://codeload.github.com/Carolnjue/pentarch-systems/zip/refs/heads/main' );

/** Download the latest code from GitHub and copy it over this plugin. Returns a message. */
function pss_self_update() {
	require_once ABSPATH . 'wp-admin/includes/file.php';
	if ( ! WP_Filesystem() ) {
		return new WP_Error( 'pss_fs', 'The server would not let WordPress write files.' );
	}
	$zip = download_url( apply_filters( 'pss_repo_zip', PSS_REPO_ZIP ) . '?t=' . time(), 180 );
	if ( is_wp_error( $zip ) ) {
		return $zip;
	}
	$dir = trailingslashit( get_temp_dir() ) . 'pss-update-' . wp_generate_password( 8, false, false );
	$res = unzip_file( $zip, $dir );
	@unlink( $zip ); // phpcs:ignore WordPress.PHP.NoSilencedErrors, WordPress.WP.AlternativeFunctions
	if ( is_wp_error( $res ) ) {
		return $res;
	}
	$src = '';
	foreach ( array_merge( array( $dir ), glob( $dir . '/*', GLOB_ONLYDIR ), glob( $dir . '/*/*', GLOB_ONLYDIR ) ) as $d ) {
		if ( file_exists( $d . '/pentarch-systems.php' ) ) {
			$src = $d;
			break;
		}
	}
	if ( ! $src ) {
		global $wp_filesystem;
		$wp_filesystem->delete( $dir, true );
		return new WP_Error( 'pss_zip', 'The download did not contain the plugin.' );
	}
	$data = get_file_data( $src . '/pentarch-systems.php', array( 'v' => 'Version' ) );
	$res  = copy_dir( $src, untrailingslashit( PSS_DIR ) );
	global $wp_filesystem;
	$wp_filesystem->delete( $dir, true );
	if ( is_wp_error( $res ) ) {
		return $res;
	}
	if ( function_exists( 'opcache_reset' ) ) {
		@opcache_reset(); // phpcs:ignore WordPress.PHP.NoSilencedErrors
	}
	update_option( 'pss_last_update', current_time( 'mysql' ) . ' · version ' . $data['v'] );
	return 'Updated from GitHub to version ' . $data['v'] . '.';
}

/* Handle the buttons (runs before the page is drawn, so new code is used for set-up on the next request). */
add_action(
	'admin_post_pss_update',
	function () {
		if ( ! current_user_can( 'manage_options' ) ) {
			wp_die( 'Not allowed.' );
		}
		check_admin_referer( 'pss_update' );
		$r   = pss_self_update();
		$msg = is_wp_error( $r ) ? 'Update failed: ' . $r->get_error_message() : $r;
		set_transient( 'pss_update_msg', $msg, 120 );
		$then = ( ! is_wp_error( $r ) && ! empty( $_POST['pss_then_setup'] ) ) ? '&pss_autosetup=' . wp_create_nonce( 'pss_autosetup' ) : '';
		wp_safe_redirect( admin_url( 'admin.php?page=pss-setup' . $then ) );
		exit;
	}
);

/* After an update, run set-up with the freshly loaded code. */
add_action(
	'admin_init',
	function () {
		if ( isset( $_GET['page'], $_GET['pss_autosetup'] ) && 'pss-setup' === $_GET['page'] && current_user_can( 'manage_options' ) && wp_verify_nonce( sanitize_key( $_GET['pss_autosetup'] ), 'pss_autosetup' ) ) {
			$rep = pss_site_setup( true );
			set_transient( 'pss_update_msg', get_transient( 'pss_update_msg' ) . ' Set-up: ' . implode( ' · ', $rep ), 120 );
			wp_safe_redirect( admin_url( 'admin.php?page=pss-setup&pss_done=1' ) );
			exit;
		}
	}
);

function pss_update_box() {
	$msg = get_transient( 'pss_update_msg' );
	if ( $msg ) {
		delete_transient( 'pss_update_msg' );
		echo '<div class="notice notice-info"><p>' . esc_html( $msg ) . '</p></div>';
	}
	echo '<div class="card" style="max-width:720px;margin:18px 0;padding:18px 22px"><h2 style="margin-top:0">Updates</h2>';
	echo '<p>Installed version <b>' . esc_html( PSS_VER ) . '</b>. Last update: ' . esc_html( get_option( 'pss_last_update', 'never' ) ) . '.</p>';
	echo '<form method="post" action="' . esc_url( admin_url( 'admin-post.php' ) ) . '">';
	wp_nonce_field( 'pss_update' );
	echo '<input type="hidden" name="action" value="pss_update">';
	echo '<p><label><input type="checkbox" name="pss_then_setup" value="1" checked> Then restore the page designs from the update</label></p>';
	echo '<p><button class="button button-primary" id="pss-update-btn">Update from GitHub</button></p></form></div>';
}
