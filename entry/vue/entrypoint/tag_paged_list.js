import Vue from 'vue';
import BannerMain from "../components/BannerMain.vue";
import TagPagedListMain from '../components/TagPagedListMain.vue';
import FooterMain from "../components/FooterMain.vue";

new Vue( {
  el: '#app-banner',
  render: h => h( BannerMain )
} );

new Vue( {
  el: '#app-list',
  render: h => h( TagPagedListMain )
} );

new Vue( {
  el: '#app-footer',
  render: h => h( FooterMain )
} );