<!--
<ScratchEditorMain>

A simple sandbox for writing MathJax+Markdown
and seeing the result in real time.
-->

<template>
    <div>
        <textarea rows="10" cols="120" v-model="text"></textarea>
        <mathjax-markdown-render :mathjax-markdown-text="text"/>
    </div>
</template>

<script>
  import MathjaxMarkdownRender from "./MathjaxMarkdownRender.vue";

  export default {
    name: "ScratchEditor",
    components: { MathjaxMarkdownRender },
    data() {
      return { text: "\\(2+2\\approx4\\)" }
    },
    watch: {
      text() {
        Vue.nextTick( () => window.MathJax.typesetPromise() );
      }
    }
  }
</script>

<style scoped>

    div {
        background-color: #ccc;
        border-radius: 2em;
        padding: 1em;
    }

    textarea {
        margin: 1em;
    }

</style>
