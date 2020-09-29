// We are in the land of webpack 4

const path = require( 'path' );

const VueLoaderPlugin = require( 'vue-loader/lib/plugin' );

//module.exports = ( env, argv ) => ({
module.exports = () => ({
  entry: {
    entry_detail: './entry/vue/entrypoint/entry_detail.js',
    entry_scratch: './entry/vue/entrypoint/scratch_editor.js',
    tag_paged_list: './entry/vue/entrypoint/tag_paged_list.js',
    entry_paged_list: './entry/vue/entrypoint/entry_paged_list.js',
    entry_tag_paged_list: './entry/vue/entrypoint/entry_tag_paged_list.js'
  },
  externals: {
    vue: 'Vue'
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        use: 'babel-loader',
        exclude: /node_modules/
      },
      {
        test: /\.vue$/,
        use: 'vue-loader'
      },
      {
        test: /\.css$/,
        use: [
          'vue-style-loader',
          'css-loader'
        ]
      }
    ]
  },
  output: {
    path: path.resolve( __dirname, 'static/vue' )
  },
  plugins: [
    new VueLoaderPlugin()
  ],
  target: "web"
});
