const path = require("path");

module.exports = {
  entry: "./src/ts/components/index.ts",
  output: {
    filename: "dashkit_kiboui.js",
    path: path.resolve(__dirname, "dashkit_kiboui"),
    library: "dashkit_kiboui",
    libraryTarget: "umd",
  },
  resolve: {
    extensions: [".ts", ".tsx", ".js", ".jsx"],
  },
  module: {
    rules: [
      {
        test: /\.tsx?$/,
        use: "ts-loader",
        exclude: /node_modules/,
      },
      {
        test: /\.css$/i,
        use: ["style-loader", "css-loader"],
      },
    ],
  },
  externals: {
    react: "React",
    "react-dom": "ReactDOM",
    "plotly.js": "Plotly",
  },
  mode: "production",
};