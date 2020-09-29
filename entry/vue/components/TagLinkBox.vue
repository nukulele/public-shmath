<---
Clicking on this link should take you to a paginated list of
entries with this tag
--->

<template>
    <a :href="`/entries/${tag.slug}/1/`">tag: <em>{{ tag.name }}</em></a>
</template>

<script>
  export default {
    name: "TagLinkBox",
    props: {
      tag: Object
    }
  }
</script>

<style scoped>

    a {
        display: inline-block;
        padding: 0.5em;
        text-decoration: none;
        background-color: lightsteelblue;
        border-radius: 0.25em;
        margin: 0 0.5em 0.5em 0;
    }
</style>