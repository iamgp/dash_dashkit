const path = require("path");

module.exports = {
  entry: "./src/ts/components/index.ts",
  output: {
    filename: "dashkit_shadcn.js",
    path: path.resolve(__dirname, "dashkit_shadcn"),
    library: "dashkit_shadcn",
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
    // recharts: "Recharts", // Bundle recharts instead of expecting it as external
  },
  mode: "production",
};