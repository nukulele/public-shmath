<template>
    <div v-if="totalPages > 1">
        <a v-if="this.pageNum > 1" :href="this.backLink">Previous Page</a> page {{ this.pageNum }} of {{ this.totalPages
        }} <a v-if="this.pageNum < this.totalPages" :href="this.nextLink">Next Page</a>
    </div>
</template>

<script>
  export default {
    name: "PaginationNavigator",
    props: {
      pageNum: Number,
      totalPages: Number,
      linkPrefix: String
    },
    computed: {
      backLink: () => {
        `${this.linkPrefix}${this.pageNum - 1}/`
      },
      nextLink: () => {
        `${this.linkPrefix}${this.pageNum + 1}/`
      }
    }
  }
</script>

<style scoped>

</style>