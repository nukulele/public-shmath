<!--
<EntryDetailDisplay>

Renders an area of MathJax + Markdown.
Styling is inherited from the parent component.
-->

<template>
    <div v-html="renderedMarkdown"></div>
</template>

<script>
  import marked from 'marked';

  export default {
    name: "MathjaxMarkdownRender",
    props: [ 'mathjaxMarkdownText' ],
    computed: {
      renderedMarkdown() {
        Vue.nextTick( () => MathJax.typeset() );
        return marked( this.mathjaxMarkdownText.replace( /\\/g, '\\\\' ) );
      }
    }
  }
</script>

<style scoped>

</style>