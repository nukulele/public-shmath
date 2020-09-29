<!--
<EntryDetailDisplay>

Renders all of an Entry Display.
Rendering of the Entry text is delegated to <MathjaxMarkdownRender>.
-->

<template>
    <div v-if="entry">
        <h1>{{ entry.name }}</h1>
        <div class="mathwrapper">
            <mathjax-markdown-render :mathjax-markdown-text="entry.text" />
        </div>
        <p v-if="entry.tags">
            <tag-link-box v-for="tag in entry.tags" :key="tag.slug" :tag="tag" />
        </p>
        <p class="small-print">This entry was created {{ dateCreateFormatted }}
            and last edited {{ dateEditFormatted }}.</p>
    </div>
</template>

<script>
  import MathjaxMarkdownRender from "./MathjaxMarkdownRender.vue";
  import TagLinkBox from "./TagLinkBox.vue";

  export default {
    name: "EntryDetailDisplay",
    components: {MathjaxMarkdownRender, TagLinkBox},
    computed: {
      dateCreateFormatted: function () {
        var d = new Date( this.entry.dateCreate );
        return d.toLocaleString()
      },
      dateEditFormatted: function () {
        var d = new Date( this.entry.dateEdit );
        return d.toLocaleString()
      }
    },
    props: {
      entry: Object
    }
  }
</script>

<style scoped>

    h1 {
        font-weight: normal;
        font-size: 3em;
        color: lightslategrey;
    }

    .mathwrapper {
        background-color: #ddd;
        padding: 1em 2em;
        border-radius: 1em;
    }

    p.small-print {
        font-size: small;
        color: lightslategrey;
    }
</style>