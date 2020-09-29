import Vue from 'vue';
import BannerMain from "../components/BannerMain.vue";
import EntryTagPagedListMain from '../components/EntryTagPagedListMain.vue';
import FooterMain from "../components/FooterMain.vue";

new Vue( {
  el: '#app-banner',
  render: h => h( BannerMain )
} );

new Vue( {
  el: '#app-list',
  render: h => h( EntryTagPagedListMain )
} );

new Vue( {
  el: '#app-footer',
  render: h => h( FooterMain )
} );