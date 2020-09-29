# virtues

- This is effectively two sites sharing models.
  - This is a site for editing `tag`s and `entry`s locally.
  - And this is a site for read-only display using Vue.
- The read-only display site should be running Vue.
- The Vue gizmo renders `markdown` and `MathJax` in the browser.
- The admin interface takes care of all the LCRUD.

### decided matters
- one mammoth SPA-like Vue gizmo for displaying lists and entries?
    - not for now
- or is it (as it is currently) a different gizmo for each page?
    - yes for now
- am I using `graphQL`, `REST`, or my hand-tooled `JSON` objects?
    - I am using `graphql`

