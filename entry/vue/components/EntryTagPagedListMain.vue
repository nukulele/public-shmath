<!--
Look for ways to streamline
Also, what if I want to send "this" per se?
-->

<template>
    <div class="entry-tag-paged-list-main" v-if="result">
        <pagination-navigator :pageNum="this.pageNum"
                              :totalPages="this.totalPages"
                              :linkPrefix="'/entries/'+this.tagSlug+'/'"/>
        <h1>tag: {{result.tag.name}}</h1>
        <entry-link-box v-for="entry in result.entries" :entry="entry" :key="entry.slug"/>
    </div>
</template>


<script>
  import axios from "axios";
  import EntryLinkBox from "./EntryLinkBox.vue";
  import PaginationNavigator from "./PaginationNavigator.vue";

  export default {
    name: "EntryPagedListMain",
    components: {
      EntryLinkBox, PaginationNavigator
    },
    data: () => ({
      pageNum: null,
      tagSlug: null,
      paginateBy: 50,
      result: null,
      totalCount: null
    }),
    computed: {
      totalPages: function () {
        if (!this.totalCount) return null;
        return Math.ceil( this.totalCount / this.paginateBy );
      }
    },
    mounted() {
      const pathParts = location.pathname.split( "/" );
      this.tagSlug = pathParts[ 2 ];
      this.pageNum = parseInt( pathParts[ 3 ] );
      axios( {
        url: '/graphql',
        method: 'post',
        data: {
          query: `
            query {
              entryCount(tag:"${this.tagSlug}")
              tag(slug:"${this.tagSlug}"){name,slug}
              entries(page:${this.pageNum},paginateBy:${this.paginateBy},tag:"${this.tagSlug}")
                { name, slug }
            }
          `
        }
      } ).then( ( result ) => {
        this.result = result.data.data;
        this.totalCount = parseInt( result.data.data.entryCount );
      } );
    }
  }
</script>


<style scoped>


    h1 {
        font-weight: normal;
        font-size: 3em;
        color: lightslategrey;
    }

    .entry-tag-paged-list-main {
        margin: 3em;
    }
</style>