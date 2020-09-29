import Vue from 'vue';
import BannerMain from "../components/BannerMain.vue";
import EntryDetailMain from '../components/EntryDetailMain.vue';
import FooterMain from "../components/FooterMain.vue";

new Vue( {
  el: '#app-banner',
  render: h => h( BannerMain )
} );

new Vue( {
  el: '#app-math',
  render: h => h( EntryDetailMain )
} );

new Vue( {
  el: '#app-footer',
  render: h => h( FooterMain )
} );