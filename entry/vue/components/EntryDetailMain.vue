<!--
<EntryDetailMain>

Handles the AJX call to get the entry information.
Display rendering is handled by <EntryDetailDisplay>.
-->

<template>
    <entry-detail-display class="entry-detail-display" :entry="entry" />
</template>

<script>
  import axios from "axios";
  import EntryDetailDisplay from "./EntryDetailDisplay.vue"

  export default {
    name: "EntryDetailMain",
    components: {
      EntryDetailDisplay
    },
    data: () => ({
      slug: null,
      entry: null
    }),
    mounted() {
      this.slug = location.pathname.slice( 1, -1 );
      axios( {
        url: '/graphql',
        method: 'post',
        data: {
          query: `
            query {
              entry(slug:"${this.slug}") {
                name, slug, text
                dateCreate, dateEdit
                tags {name, slug}
              }
            }
          `
        }
      } ).then( ( result ) => {
        this.entry = result.data.data.entry;
      } );
    }
  }
</script>

<style scoped>

    .entry-detail-display {
        margin: 3em;
    }

</style>