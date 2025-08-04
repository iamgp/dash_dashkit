const path = require('path');

module.exports = {
  entry: './src/ts/components/index.ts',
  output: {
    filename: 'dash_attio_table.js',
    path: path.resolve(__dirname, 'dash_attio_table'),
    library: 'dash_attio_table',
    libraryTarget: 'umd'
  },
  resolve: {
    extensions: ['.ts', '.tsx', '.js', '.jsx']
  },
  module: {
    rules: [
      {
        test: /\.tsx?$/,
        use: 'ts-loader',
        exclude: /node_modules/
      },
      {
        test: /\.css$/i,
        use: ['style-loader', 'css-loader']
      }
    ]
  },
  externals: {
    'react': 'React',
    'react-dom': 'ReactDOM',
    'plotly.js': 'Plotly'
  }
};