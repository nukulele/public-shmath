<!--
<FooterMain>

Hey, Sugar. Tell 'em who we are.
-->

<template>
    <div class="banner-main">
        <h1>math, shmath</h1>
        <div class="navigation-links-bar">
            <entry-link-box :entry="{name:'shmath home page',slug:'home'}"/>
        </div>
    </div>
</template>

<script>
  import EntryLinkBox from "./EntryLinkBox.vue";
  import TagLinkBox from "./TagLinkBox.vue";

  export default {
    name: "BannerMain",
    components: {
      EntryLinkBox, TagLinkBox
    }
  }
</script>

<style scoped>

    .banner-main {
        margin: 0;
        background-color: lightgrey;
    }

    h1 {
        font-weight: normal;
        margin: 0;
        color: lightslategrey;
        padding: 0.5em;
    }

    .navigation-links-bar {
        font-weight: normal;
    }
</style>
