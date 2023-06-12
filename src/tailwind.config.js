module.exports = {
    content: {
        relative: true,
        files: [
            './**/templates/*.html',
            './**/templates/**/*.html',
        ]
    },
    theme: {
        extend: {
            colors: {
                jet: '#2A2B2E'
            },
            fontFamily: {
                sans: ['Poppins', 'Inter', 'sans-serif'],
                heading: ['Barlow Condensed', 'Inter', 'sans-serif']
            }
        },
    }
};