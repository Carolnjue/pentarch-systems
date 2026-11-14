<?php
/**
 * Demo and quote requests: the form, saving, email notice and the admin list.
 */
if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

function pss_products() {
	return array(
		'medicore' => 'Pentarch MediCore (pharmacy, clinic or hospital)',
		'pos' => 'Pentarch POS (shops and businesses)',
		'complyscope' => 'ComplyScope Kenya (business compliance)',
		'portal' => 'Pentarch Portal (school or college)',
		'beautysuite' => 'Pentarch BeautySuite (salon or spa)',
		'learning' => 'Courses and learning system',
		'simlab' => 'Pentarch SimLab (virtual labs for courses)',
		'qr' => 'Pentarch QR Analytics (campaigns and print)',
		'liveedit' => 'Pentarch Live Edit (edit my site on the page)',
		'website' => 'A new website or a website revamp',
		'interactive' => 'Interactive or 3D experience',
		'data' => 'Dashboards and StoryMaps',
		'custom' => 'A custom system',
		'agent' => 'I want to become a sales agent',
		'other' => 'Something else',
	);
}

add_action(
	'init',
	function () {
		register_post_type(
			'pss_lead',
			array(
				'labels'       => array(
					'name'          => 'Demo requests',
					'singular_name' => 'Demo request',
					'menu_name'     => 'Demo requests',
					'all_items'     => 'All requests',
					'edit_item'     => 'Request',
				),
				'public'       => false,
				'show_ui'      => true,
				'menu_icon'    => 'dashicons-email-alt',
				'supports'     => array( 'title', 'editor' ),
				'capabilities' => array( 'create_posts' => 'do_not_allow' ),
				'map_meta_cap' => true,
			)
		);
		if ( isset( $_POST['pss_lead_nonce'] ) ) { // phpcs:ignore WordPress.Security.NonceVerification
			pss_handle_lead();
		}
	}
);

function pss_handle_lead() {
	$back = wp_get_referer() ? wp_get_referer() : home_url( '/contact/' );
	$back = remove_query_arg( array( 'sent', 'err' ), $back );
	if ( ! wp_verify_nonce( sanitize_text_field( wp_unslash( $_POST['pss_lead_nonce'] ) ), 'pss_lead' ) ) {
		wp_safe_redirect( add_query_arg( 'err', 'expired', $back ) . '#pss-form' );
		exit;
	}
	$f = function ( $k ) {
		return isset( $_POST[ $k ] ) ? sanitize_text_field( wp_unslash( $_POST[ $k ] ) ) : ''; // phpcs:ignore WordPress.Security.NonceVerification
	};
	if ( '' !== $f( 'website' ) ) { // honeypot.
		wp_safe_redirect( add_query_arg( 'sent', '1', $back ) . '#pss-form' );
		exit;
	}
	$d = array(
		'product' => $f( 'product' ),
		'org'     => $f( 'org' ),
		'name'    => $f( 'name' ),
		'phone'   => $f( 'phone' ),
		'email'   => sanitize_email( $f( 'email' ) ),
		'town'    => $f( 'town' ),
		'when'    => $f( 'when' ),
		'message' => isset( $_POST['message'] ) ? sanitize_textarea_field( wp_unslash( $_POST['message'] ) ) : '', // phpcs:ignore WordPress.Security.NonceVerification
	);
	if ( '' === $d['name'] || '' === $d['phone'] ) {
		wp_safe_redirect( add_query_arg( 'err', 'missing', $back ) . '#pss-form' );
		exit;
	}
	$all   = pss_products();
	$label = isset( $all[ $d['product'] ] ) ? $all[ $d['product'] ] : 'General enquiry';
	$id    = wp_insert_post(
		array(
			'post_type'    => 'pss_lead',
			'post_status'  => 'private',
			'post_title'   => $d['name'] . ( $d['org'] ? ' — ' . $d['org'] : '' ) . ' · ' . $label,
			'post_content' => $d['message'],
		)
	);
	if ( $id && ! is_wp_error( $id ) ) {
		foreach ( $d as $k => $v ) {
			update_post_meta( $id, '_pss_' . $k, $v );
		}
	}
	$to   = get_option( 'pss_notify', 'info@pentarchsystemssolutions.co.ke' );
	$body = "New request from the Pentarch Systems Solutions website\n\n"
		. "Interested in: $label\nOrganisation: {$d['org']}\nName: {$d['name']}\nPhone: {$d['phone']}\nEmail: {$d['email']}\nTown: {$d['town']}\nPreferred time: {$d['when']}\n\nMessage:\n{$d['message']}\n\n"
		. 'All requests: ' . admin_url( 'edit.php?post_type=pss_lead' );
	$headers = $d['email'] ? array( 'Reply-To: ' . $d['name'] . ' <' . $d['email'] . '>' ) : array();
	wp_mail( $to, 'Demo request: ' . $label . ' — ' . $d['name'], $body, $headers );
	wp_safe_redirect( add_query_arg( 'sent', '1', $back ) . '#pss-form' );
	exit;
}

/* The form: [pss_lead_form product="medicore" button="Book my demo"] */
add_shortcode(
	'pss_lead_form',
	function ( $a ) {
		$a    = shortcode_atts( array( 'product' => '', 'button' => 'Book my demo' ), $a );
		$sel  = isset( $_GET['product'] ) ? sanitize_key( wp_unslash( $_GET['product'] ) ) : $a['product']; // phpcs:ignore WordPress.Security.NonceVerification
		if ( '' === $sel ) {
			$sel = 'other';
		}
		$sent = isset( $_GET['sent'] ); // phpcs:ignore WordPress.Security.NonceVerification
		$err  = isset( $_GET['err'] ) ? sanitize_key( wp_unslash( $_GET['err'] ) ) : ''; // phpcs:ignore WordPress.Security.NonceVerification
		if ( $sent ) {
			return '<div class="tf" id="pss-form"><div class="ok">' . pss_icon( 'check' ) . '<h3>Thank you. We have your request.</h3><p>A member of the Pentarch Systems team will call or WhatsApp you within one working day to agree a time for your demo.</p><a class="btn btn-d" style="justify-content:center" href="https://wa.me/254729455912?text=Hello%20Pentarch%20Systems%2C%20I%20just%20sent%20a%20demo%20request." target="_blank" rel="noopener">' . pss_icon( 'wa' ) . ' Continue on WhatsApp</a></div></div>';
		}
		$o = '<form class="tf" id="pss-form" method="post" action="">';
		if ( $err ) {
			$o .= '<div class="err" style="display:block">' . ( 'missing' === $err ? 'Please give your name and phone number.' : 'The form expired. Please send it again.' ) . '</div>';
		}
		$o .= wp_nonce_field( 'pss_lead', 'pss_lead_nonce', false, false );
		$o .= '<label>I am interested in<select name="product">';
		foreach ( pss_products() as $k => $v ) {
			$o .= '<option value="' . esc_attr( $k ) . '"' . selected( $sel, $k, false ) . '>' . esc_html( $v ) . '</option>';
		}
		$o .= '</select></label>';
		$eg = array( 'medicore' => 'Afya Bora Chemist', 'pos' => 'Mama Njeri Supermarket', 'portal' => 'Machakos Training College', 'beautysuite' => 'Glow Salon and Spa', 'learning' => 'Kilimani Training Centre', 'simlab' => 'Rift Valley Technical College', 'ngo' => 'Hope for Children Trust', 'qr' => 'Green Valley Campaign', 'complyscope' => 'Baraka Hardware Ltd' );
		$o .= '<label>Organisation or business<input name="org" placeholder="e.g. ' . esc_attr( $eg[ $sel ] ?? 'Your organisation' ) . '" autocomplete="organization"></label>';
		$o .= '<div class="r2"><label>Your name<input name="name" required autocomplete="name"></label><label>Phone<input name="phone" required inputmode="tel" placeholder="07…" autocomplete="tel"></label></div>';
		$o .= '<div class="r2"><label>Email (optional)<input name="email" type="email" autocomplete="email"></label><label>Town<input name="town" placeholder="e.g. Nairobi"></label></div>';
		$o .= '<label>Best time for a demo<select name="when"><option>Any weekday</option><option>Weekday morning</option><option>Weekday afternoon</option><option>Saturday</option></select></label>';
		$o .= '<label>Tell us a little about what you need (optional)<textarea name="message" rows="4" placeholder="Number of branches, staff or students, what you use today…"></textarea></label>';
		$o .= '<div class="hp" aria-hidden="true"><label>Website<input name="website" tabindex="-1" autocomplete="off"></label></div>';
		$o .= '<button class="go" type="submit">' . esc_html( $a['button'] ) . ' ' . pss_icon( 'arrow' ) . '</button>';
		$o .= '<p style="font-size:13px;color:var(--mute);text-align:center">We reply within one working day. Your details are only used to arrange your demo.</p>';
		return $o . '</form>';
	}
);

/* Admin list columns. */
add_filter(
	'manage_pss_lead_posts_columns',
	function ( $c ) {
		return array(
			'cb'       => $c['cb'],
			'title'    => 'Request',
			'pss_ph'   => 'Phone',
			'pss_town' => 'Town',
			'date'     => 'Received',
		);
	}
);
add_action(
	'manage_pss_lead_posts_custom_column',
	function ( $col, $id ) {
		if ( 'pss_ph' === $col ) {
			$ph = get_post_meta( $id, '_pss_phone', true );
			$wa = preg_replace( '/^0/', '254', preg_replace( '/\D/', '', $ph ) );
			echo esc_html( $ph ) . ( $wa ? ' · <a href="https://wa.me/' . esc_attr( $wa ) . '" target="_blank" rel="noopener">WhatsApp</a>' : '' );
		}
		if ( 'pss_town' === $col ) {
			echo esc_html( get_post_meta( $id, '_pss_town', true ) );
		}
	},
	10,
	2
);
add_action(
	'add_meta_boxes',
	function () {
		add_meta_box(
			'pss_lead_box',
			'Request details',
			function ( $post ) {
				$labels = array( 'product' => 'Interested in', 'org' => 'Organisation', 'name' => 'Name', 'phone' => 'Phone', 'email' => 'Email', 'town' => 'Town', 'when' => 'Preferred time' );
				$all    = pss_products();
				echo '<table class="widefat striped">';
				foreach ( $labels as $k => $l ) {
					$v = get_post_meta( $post->ID, '_pss_' . $k, true );
					if ( 'product' === $k && isset( $all[ $v ] ) ) {
						$v = $all[ $v ];
					}
					echo '<tr><th style="width:160px">' . esc_html( $l ) . '</th><td>' . esc_html( $v ) . '</td></tr>';
				}
				echo '</table>';
			},
			'pss_lead',
			'normal',
			'high'
		);
	}
);

/*
 * The page designs are Live Edit blocks, and WordPress does not expand shortcodes nested inside
 * another shortcode's output. Render the demo form wherever a block places it.
 */
function pss_render_nested_forms( $html ) {
	if ( false === strpos( (string) $html, '[pss_lead_form' ) ) {
		return $html;
	}
	return preg_replace_callback(
		'/\[pss_lead_form[^\]]*\]/',
		function ( $m ) {
			return do_shortcode( $m[0] );
		},
		$html
	);
}
add_filter( 'the_content', 'pss_render_nested_forms', 20 );
