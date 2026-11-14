<?php
/**
 * Page not found: same header and footer as the rest of the site, with the main ways in.
 */
if ( ! defined( 'ABSPATH' ) ) {
	exit;
}
status_header( 404 );
$pss_links = array(
	array( '/products/', 'layers', 'Products', 'MediCore, POS, ComplyScope, Portal and more' ),
	array( '/services/', 'cog', 'Services', 'Websites, systems, 3D, dashboards and integrations' ),
	array( '/work/', 'star', 'Our work', 'Systems and sites in use today' ),
	array( '/contact/', 'call', 'Contact us', 'Phone, WhatsApp or a demo request' ),
);
?><!doctype html>
<html <?php language_attributes(); ?>>
<head>
<meta charset="<?php bloginfo( 'charset' ); ?>">
<?php ob_start(); wp_head(); $pss_head = ob_get_clean(); if ( false === stripos( $pss_head, 'name="viewport"' ) ) { echo '<meta name="viewport" content="width=device-width, initial-scale=1">' . "\n"; } echo $pss_head; // phpcs:ignore WordPress.Security.EscapeOutput ?>
</head>
<body <?php body_class( 'pss-canvas' ); ?>>
<?php wp_body_open(); ?>
<main id="pss-content">
<div class="pss pss-page pg-404" id="pss-main">
<section class="hero t-ink hero-404"><div class="hero-grid" aria-hidden="true"></div><div class="wrap">
<p class="hs-k"><span class="ic"><?php echo pss_icon( 'search' ); // phpcs:ignore ?></span>Error 404</p>
<h1>This page is not here.</h1>
<p class="hero-p">The address may have changed when the site was reorganised. These are the main ways in.</p>
<ul class="caps nf-links">
<?php foreach ( $pss_links as $l ) : ?>
<li><a href="<?php echo esc_url( home_url( $l[0] ) ); ?>"><span class="ic"><?php echo pss_icon( $l[1] ); // phpcs:ignore ?></span><h3><?php echo esc_html( $l[2] ); ?></h3><p><?php echo esc_html( $l[3] ); ?></p></a></li>
<?php endforeach; ?>
</ul>
<div class="btns"><a class="btn btn-p" href="<?php echo esc_url( home_url( '/' ) ); ?>">Go to the home page <span class="ic"><?php echo pss_icon( 'arrow' ); // phpcs:ignore ?></span></a></div>
</div></section>
</div>
</main>
<?php wp_footer(); ?>
</body>
</html>
