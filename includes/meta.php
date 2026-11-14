<?php
/**
 * Search and sharing: a description, Open Graph and Twitter tags for each page of the site.
 */
if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

function pss_meta_map() {
	return array(
		'home'         => array( 'Systems Kenyan organisations run on: MediCore for health facilities, Pentarch POS, ComplyScope, school portals and websites your team edits itself. Built and supported in Nairobi.', 'mc-dashboard' ),
		'products'     => array( 'Seven products in daily use: MediCore, Pentarch POS, ComplyScope Kenya, Portal, BeautySuite, QR Analytics and Live Edit. Compare them and book a demo.', 'pos-home' ),
		'medicore'     => array( 'Pentarch MediCore runs a pharmacy, clinic or hospital on one system, with or without internet: counter, patients, lab, wards, billing, SHA and stock. Try it free for 30 days.', 'mc-dashboard' ),
		'pos'          => array( 'Pentarch POS: an offline till for Kenyan shops, chemists, hardware stores, restaurants and bars, with M-Pesa, KRA tax codes, credit book and Kiswahili. Try the live demo.', 'pos-sell' ),
		'complyscope'  => array( 'ComplyScope Kenya maps every filing, permit and renewal a Kenyan business owes, national and county, scores your compliance and keeps a dossier ready for inspectors.', 'cs-overview' ),
		'portal'       => array( 'Pentarch Portal: admissions, fees, LMS, exams, certificates with QR verification and alumni, running inside your own college website.', 'portal-dashboard' ),
		'beautysuite'  => array( 'Pentarch BeautySuite: front desk, bookings, bridal packages and fair staff commissions for salons, barbers and spas.', 'salon-desk' ),
		'learning'     => array( 'Course catalogues that fill classes: schools, class dates with seats left, registration with M-Pesa, group rates and Moodle support for training institutes.', 'pti-intake' ),
		'qr-analytics' => array( 'Pentarch QR Analytics: trackable QR codes for printed campaigns, with scans by date, device and country, and client reports.', 'qr-dashboard' ),
		'live-edit'    => array( 'Pentarch Live Edit: a custom-designed website that your team edits by clicking on the page, with a revision for every save.', 'live-edit' ),
		'services'     => array( 'Websites, custom systems and portals, interactive and 3D, dashboards and StoryMaps, and integrations with M-Pesa, KRA eTIMS, WhatsApp, SMS and AI assistants.', 'portal-dashboard' ),
		'labs'         => array( 'Websites people stay on: 3D showrooms, engine cutaways, games, parts finders, calculators and planners that run in an ordinary browser.', 'laqim-showroom' ),
		'simlab'       => array( 'Pentarch SimLab: more than 50 interactive simulations for college and university students, free and running in any browser.', 'sim-home' ),
		'data-maps'    => array( 'ArcGIS StoryMaps, interactive dashboards and campaign analytics that turn field data and programme results into pages people read.', 'sm-map' ),
		'websites'     => array( 'Ten websites built by Pentarch, each edited by its owner with Live Edit: colleges, consultancies, a car showcase, a media agency and an internet provider.', 'site-glamourvine' ),
		'work'         => array( 'Systems and websites in use today: MediCore pilots, Glamourvine, Laqim Autoworld, Pentarch Training Institute, Zingira Pesa and AMALNA South Sudan.', 'agile' ),
		'about'        => array( 'Pentarch Systems Solutions builds, installs and supports software for Kenyan organisations. Part of the Pentarch family, based in Nairobi.', 'pti-intake' ),
		'contact'      => array( 'Book a demo or talk to the Pentarch Systems Solutions team in Nairobi by phone, WhatsApp or email.', 'mc-dashboard' ),
	);
}

add_action(
	'wp_head',
	function () {
		if ( ! is_page() && ! is_front_page() ) {
			return;
		}
		$p    = get_queried_object();
		$slug = is_front_page() ? 'home' : ( $p && isset( $p->post_name ) ? $p->post_name : '' );
		$map  = pss_meta_map();
		if ( ! isset( $map[ $slug ] ) ) {
			return;
		}
		list( $desc, $shot ) = $map[ $slug ];
		$img   = PSS_URL . 'assets/img/pss-shot-' . $shot . '.jpg';
		$title = wp_get_document_title();
		$url   = is_front_page() ? home_url( '/' ) : get_permalink( $p );
		echo "\n" . '<meta name="description" content="' . esc_attr( $desc ) . '">' . "\n";
		echo '<meta property="og:type" content="website">' . "\n";
		echo '<meta property="og:site_name" content="Pentarch Systems Solutions">' . "\n";
		echo '<meta property="og:title" content="' . esc_attr( $title ) . '">' . "\n";
		echo '<meta property="og:description" content="' . esc_attr( $desc ) . '">' . "\n";
		echo '<meta property="og:url" content="' . esc_url( $url ) . '">' . "\n";
		echo '<meta property="og:image" content="' . esc_url( $img ) . '">' . "\n";
		echo '<meta property="og:locale" content="en_GB">' . "\n";
		echo '<meta name="twitter:card" content="summary_large_image">' . "\n";
		echo '<meta name="theme-color" content="#0A1530">' . "\n";
	},
	2
);

/* The canvas template prints its own viewport tag; drop WordPress's block-theme duplicate on these pages. */
add_action(
	'wp',
	function () {
		if ( is_singular( 'page' ) && 'pss-canvas' === get_page_template_slug( get_queried_object_id() ) ) {
			remove_action( 'wp_head', '_block_template_viewport_meta_tag', 0 );
		}
	}
);

/* Pages kept only to forward old addresses stay out of search. */
function pss_moved_page_ids() {
	$ids = array();
	foreach ( array( 'solutions', 'dashboards', 'ngo-portal' ) as $s ) {
		$p = get_page_by_path( $s );
		if ( $p ) {
			$ids[] = (int) $p->ID;
		}
	}
	return $ids;
}
add_filter(
	'wp_sitemaps_posts_query_args',
	function ( $args, $type ) {
		if ( 'page' === $type ) {
			$args['post__not_in'] = array_merge( isset( $args['post__not_in'] ) ? (array) $args['post__not_in'] : array(), pss_moved_page_ids() );
		}
		return $args;
	},
	10,
	2
);
add_filter(
	'wp_robots',
	function ( $r ) {
		if ( is_page() && in_array( (int) get_queried_object_id(), pss_moved_page_ids(), true ) ) {
			$r['noindex'] = true;
		}
		return $r;
	}
);
