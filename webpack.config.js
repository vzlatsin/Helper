const path = require('path');

module.exports = {
    entry: {
        bundle: './src/index.js',
        task_diary: './src/components/task_diary.js',
        todays_tasks: './src/components/todays_tasks.js',
        tabs: './src/components/tabs.js',
        backlog: './src/components/backlog.js'
    },
    output: {
        filename: '[name].js',
        path: path.resolve(__dirname, 'static')
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: ['@babel/preset-env', '@babel/preset-react']
                    }
                }
            }
        ]
    },
    mode: 'development',
    watch: true // Enable watch mode
};
