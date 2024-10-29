module.exports = {
    content: [
        // Paths to Django templates
        '../templates/**/*.html',
        '../../templates/**/*.html',
        '../../**/templates/**/*.html',
        '../../**/*.js',  // Uncomment if using Tailwind in JavaScript files
    ],
    theme: {
        extend: {},
    },
    plugins: [
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/aspect-ratio'),
    ],
    corePlugins: {
        preflight: false, // disables Tailwind's base styles
    },
}
