var path = require('path');

module.exports = {
    entry: './src/js/index.js',
    output: {
        filename: 'index.js',
        path: path.join(__dirname, '/app/static/js')
    },
    module: {
        rules: [
            {
                test: /\.(scss)$/,
                use: ['style-loader', 'css-loader', 'sass-loader'],
            }
        ]
    }
}