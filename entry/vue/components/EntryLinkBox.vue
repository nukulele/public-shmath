<---
Clicking on this link should take you to the
entry detail display for this entry.
--->

<template>
    <a :href="`/${entry.slug}/`">{{ entry.name }}</a>
</template>

<script>
  export default {
    name: "EntryLinkBox",
    props: {
      entry: Object
    }
  }
</script>

<style scoped>

    a {
        display: inline-block;
        padding: 0.5em;
        text-decoration: none;
        background-color: lightgrey;
        border-radius: 0.25em;
        margin: 0 0.5em 0.5em 0;
    }
</style>