<!--
Look for ways to streamline
Also, what if I want to send "this" per se?
-->

<template>
    <div class="entry-paged-list-main" v-if="result">
        <pagination-navigator :pageNum="this.pageNum" :totalPages="this.totalPages" :linkPrefix="'/entries/'"/>
        <h1>index of entries</h1>
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
    data: () => ( {
      pageNum: null,
      paginateBy: 100,
      result: null,
      totalCount: null
    } ),
    computed: {
      totalPages: function () {
        if (!this.totalCount) return null;
        return Math.ceil( this.totalCount / this.paginateBy );
      }
    },
    mounted() {
      const pathstring = location.pathname;
      this.pageNum = parseInt( pathstring.split( "/" )[2] );
      axios( {
        url: '/graphql',
        method: 'post',
        data: {
          query: `
            query {
              entryCount
              entries(page:${this.pageNum},paginateBy:${this.paginateBy})
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

    .entry-paged-list-main {
        margin: 3em;
    }
</style>