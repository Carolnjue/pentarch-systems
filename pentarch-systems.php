<?php
/**
 * Plugin Name:       Pentarch Systems Solutions Site
 * Description:       The Pentarch Systems Solutions website: page designs, header and footer (edited with Pentarch Live Edit), demo requests and the site set-up.
 * Version:           1.3.2
 * Requires at least: 6.2
 * Requires PHP:      7.4
 * Author:            Pentarch Systems Solutions
 * Author URI:        https://pentarchcommunications.com
 * Text Domain:       pentarch-systems
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

define( 'PSS_VER', '1.3.2' );
define( 'PSS_DIR', plugin_dir_path( __FILE__ ) );
define( 'PSS_URL', plugin_dir_url( __FILE__ ) );

/* ------------------------------------------------------------------ icons */

function pss_icon( $name ) {
	static $p = null;
	if ( null === $p ) {
		$p = array(
			'arrow'   => '<path d="M5 12h14M13 6l6 6-6 6"/>',
			'ne'      => '<path d="M7 17 17 7M8 7h9v9"/>',
			'chev'    => '<path d="m6 9 6 6 6-6"/>',
			'menu'    => '<path d="M4 7h16M4 12h16M4 17h10"/>',
			'x'       => '<path d="M18 6 6 18M6 6l12 12"/>',
			'up'      => '<path d="m18 15-6-6-6 6"/>',
			'check'   => '<path d="M20 6 9 17l-5-5"/>',
			'call'    => '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/>',
			'mail'    => '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/>',
			'pin'     => '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/>',
			'wa'      => '<path d="M3 21l1.6-4.7A9 9 0 1 1 8 19.6z"/><path d="M9 9.5c0 3 2.5 5.5 5.5 5.5l1.2-1.4-2-1-1 .8a4 4 0 0 1-2.1-2.1l.8-1-1-2z"/>',
			'health'  => '<rect x="3" y="3" width="18" height="18" rx="4"/><path d="M12 8v8M8 12h8"/>',
			'school'  => '<path d="M22 10 12 5 2 10l10 5 10-5z"/><path d="M6 12v5c3 2 9 2 12 0v-5"/>',
			'scissor' => '<circle cx="6" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><path d="M20 4 8.1 15.9M14.5 14.5 20 20M8.1 8.1 12 12"/>',
			'cart'    => '<circle cx="9" cy="20" r="1.5"/><circle cx="18" cy="20" r="1.5"/><path d="M2 3h3l2.6 12.4a2 2 0 0 0 2 1.6h8.8a2 2 0 0 0 2-1.6L22 7H6"/>',
			'pen'     => '<path d="M12 20h9"/><path d="M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4z"/>',
			'book'    => '<path d="M2 4h7a3 3 0 0 1 3 3v14a2 2 0 0 0-2-2H2z"/><path d="M22 4h-7a3 3 0 0 0-3 3v14a2 2 0 0 1 2-2h8z"/>',
			'web'     => '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 9h18M10 13l-2 2 2 2M14 13l2 2-2 2"/>',
			'map'     => '<path d="m3 6 6-3 6 3 6-3v15l-6 3-6-3-6 3z"/><path d="M9 3v15M15 6v15"/>',
			'chart'   => '<path d="M3 3v18h18"/><path d="m7 15 4-4 3 3 5-6"/>',
			'wifi'    => '<path d="M5 12.5a10 10 0 0 1 14 0M8.5 16a5 5 0 0 1 7 0"/><path d="M2 9a15 15 0 0 1 20 0"/><circle cx="12" cy="19.5" r="1"/>',
			'offline' => '<path d="M2 2l20 20"/><path d="M8.5 16a5 5 0 0 1 7 0M5 12.5a10 10 0 0 1 4.2-2.6M2 9a15 15 0 0 1 4.5-2.9M12 4.5a15 15 0 0 1 10 4.5"/><circle cx="12" cy="19.5" r="1"/>',
			'phone'   => '<rect x="6" y="2" width="12" height="20" rx="3"/><path d="M11 18h2"/>',
			'shield'  => '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/>',
			'lock'    => '<rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>',
			'users'   => '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8"/>',
			'server'  => '<rect x="2" y="3" width="20" height="8" rx="2"/><rect x="2" y="13" width="20" height="8" rx="2"/><path d="M6 7h.01M6 17h.01"/>',
			'cloud'   => '<path d="M17.5 19a4.5 4.5 0 1 0-1.4-8.8A6 6 0 1 0 6 17.2"/><path d="M6 19h11.5"/>',
			'cash'    => '<rect x="2" y="6" width="20" height="12" rx="2"/><circle cx="12" cy="12" r="2.5"/><path d="M6 12h.01M18 12h.01"/>',
			'box'     => '<path d="M21 8 12 3 3 8v8l9 5 9-5z"/><path d="M3 8l9 5 9-5M12 13v8"/>',
			'scan'    => '<path d="M3 7V5a2 2 0 0 1 2-2h2M17 3h2a2 2 0 0 1 2 2v2M21 17v2a2 2 0 0 1-2 2h-2M7 21H5a2 2 0 0 1-2-2v-2"/><path d="M7 8v8M10 8v8M13 8v8M17 8v8"/>',
			'print'   => '<path d="M6 9V2h12v7"/><rect x="2" y="9" width="20" height="9" rx="2"/><path d="M6 14h12v8H6z"/>',
			'monitor' => '<rect x="2" y="3" width="20" height="14" rx="2"/><path d="M8 21h8M12 17v4"/>',
			'battery' => '<rect x="2" y="7" width="17" height="10" rx="2"/><path d="M22 11v2M6 10l-1 4M9 10l-1 4"/>',
			'lab'     => '<path d="M9 3h6"/><path d="M10 3v6.5L4.6 18.2A1.9 1.9 0 0 0 6.2 21h11.6a1.9 1.9 0 0 0 1.6-2.8L14 9.5V3"/><path d="M7.5 15h9"/>',
			'bed'     => '<path d="M2 4v16M2 8h18a2 2 0 0 1 2 2v10M2 17h20"/><path d="M6 8v9"/>',
			'pill'    => '<path d="m10.5 20.5 10-10a4.9 4.9 0 0 0-7-7l-10 10a4.9 4.9 0 0 0 7 7z"/><path d="m8.5 8.5 7 7"/>',
			'cal'     => '<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>',
			'star'    => '<path d="m12 2 3.1 6.3 6.9 1-5 4.9 1.2 6.8L12 17.8 5.8 21l1.2-6.8-5-4.9 6.9-1z"/>',
			'layers'  => '<path d="m12 2 10 5-10 5L2 7z"/><path d="m2 17 10 5 10-5M2 12l10 5 10-5"/>',
			'code'    => '<path d="m16 18 6-6-6-6M8 6l-6 6 6 6"/>',
			'search'  => '<circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/>',
			'globe'   => '<circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15 15 0 0 1 0 20M12 2a15 15 0 0 0 0 20"/>',
			'cog'     => '<circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.7 1.7 0 0 0 .3 1.8l.1.1a2 2 0 1 1-2.8 2.8l-.1-.1a1.7 1.7 0 0 0-1.8-.3 1.7 1.7 0 0 0-1 1.5V21a2 2 0 1 1-4 0v-.1a1.7 1.7 0 0 0-1.1-1.5 1.7 1.7 0 0 0-1.8.3l-.1.1a2 2 0 1 1-2.8-2.8l.1-.1a1.7 1.7 0 0 0 .3-1.8 1.7 1.7 0 0 0-1.5-1H3a2 2 0 1 1 0-4h.1a1.7 1.7 0 0 0 1.5-1.1 1.7 1.7 0 0 0-.3-1.8l-.1-.1a2 2 0 1 1 2.8-2.8l.1.1a1.7 1.7 0 0 0 1.8.3H9a1.7 1.7 0 0 0 1-1.5V3a2 2 0 1 1 4 0v.1a1.7 1.7 0 0 0 1 1.5 1.7 1.7 0 0 0 1.8-.3l.1-.1a2 2 0 1 1 2.8 2.8l-.1.1a1.7 1.7 0 0 0-.3 1.8V9a1.7 1.7 0 0 0 1.5 1H21a2 2 0 1 1 0 4h-.1a1.7 1.7 0 0 0-1.5 1z"/>',
			'spark'   => '<path d="M12 3v4M12 17v4M3 12h4M17 12h4M5.6 5.6l2.8 2.8M15.6 15.6l2.8 2.8M5.6 18.4l2.8-2.8M15.6 8.4l2.8-2.8"/>',
			'handshake' => '<path d="m11 17 2 2a1 1 0 1 0 3-3"/><path d="m14 14 2.5 2.5a1 1 0 1 0 3-3l-3.9-3.9a2 2 0 0 0-2.8 0l-.9.9a1 1 0 1 1-3-3l2.8-2.8a5.8 5.8 0 0 1 7.1-.9l.5.3a2 2 0 0 0 1.4.2L21 4"/><path d="m21 3 1 11h-2M3 3 2 14l6.5 6.5a1 1 0 1 0 3-3M3 4h8"/>',
			'clock'   => '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
			'play'    => '<path d="m6 4 14 8-14 8z"/>',
		);
	}
	if ( ! isset( $p[ $name ] ) ) {
		$name = 'spark';
	}
	return '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' . $p[ $name ] . '</svg>';
}

/* --------------------------------------------------------------- assets */

add_action(
	'wp_enqueue_scripts',
	function () {
		wp_enqueue_style( 'pss-fonts', 'https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,600;12..96,700;12..96,800&family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;1,9..40,400&family=JetBrains+Mono:wght@500;600&display=swap', array(), null );
		wp_enqueue_style( 'pss', PSS_URL . 'assets/pss.css', array(), PSS_VER );
		wp_enqueue_script( 'pss', PSS_URL . 'assets/pss.js', array(), PSS_VER, true );
	}
);

add_action(
	'wp_head',
	function () {
		echo "<script>document.documentElement.classList.add('pc-js');setTimeout(function(){if(!window.PC_OK)document.documentElement.classList.add('pc-failsafe')},3000);</script>\n";
		echo '<style>.site-header,.site-footer,#masthead,#colophon,header.wp-block-template-part,footer.wp-block-template-part{display:none!important}</style>' . "\n";
	},
	2
);

/* ----------------------------------------------------- full-width canvas */

add_filter(
	'theme_page_templates',
	function ( $t ) {
		$t['pss-canvas'] = 'Pentarch Systems full width (no theme header/footer)';
		return $t;
	}
);
add_filter(
	'template_include',
	function ( $tpl ) {
		if ( is_singular( 'page' ) && 'pss-canvas' === get_page_template_slug( get_queried_object_id() ) ) {
			return PSS_DIR . 'templates/canvas.php';
		}
		return $tpl;
	},
	99
);
add_filter(
	'body_class',
	function ( $c ) {
		if ( is_singular( 'page' ) && 'pss-canvas' === get_page_template_slug( get_queried_object_id() ) ) {
			$c[] = 'pss-canvas';
		}
		return $c;
	}
);

require_once PSS_DIR . 'includes/leads.php';
require_once PSS_DIR . 'includes/setup.php';
require_once PSS_DIR . 'includes/updater.php';
