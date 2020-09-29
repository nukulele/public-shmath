<!--
Look for ways to streamline
Also, what if I want to send "this" per se?
-->

<template>
    <div class="tag-paged-list-main" v-if="result">
        <pagination-navigator :pageNum="this.pageNum" :totalPages="this.totalPages" :linkPrefix="'/tags/'"/>
        <h1>index of tags</h1>
        <tag-link-box v-for="tag in result.tags" :tag="tag" :key="tag.slug"/>
    </div>
</template>


<script>
  import axios from "axios";
  import TagLinkBox from "./TagLinkBox.vue";
  import PaginationNavigator from "./PaginationNavigator.vue";

  export default {
    name: "TagPagedListMain",
    components: {
      TagLinkBox, PaginationNavigator
    },
    data: () => ({
      pageNum: null,
      paginateBy: 500,
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
      const pathstring = location.pathname;
      this.pageNum = parseInt( pathstring.split( "/" )[ 2 ] );
      axios( {
        url: '/graphql',
        method: 'post',
        data: {
          query: `
            query {
              tagCount
              tags(page:${this.pageNum},paginateBy:${this.paginateBy})
                { name, slug }
            }
          `
        }
      } ).then( ( result ) => {
        this.result = result.data.data;
        this.totalCount = parseInt( result.data.data.tagCount );
      } );
    }
  }
</script>


<style scoped>
    .tag-paged-list-main {
        margin: 3em;
    }

    h1 {
        font-weight: normal;
        font-size: 3em;
        color: lightslategrey;
    }
</style>