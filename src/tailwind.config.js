module.exports = {
    content: {
        relative: true,
        files: [
            './**/templates/*.html',
            './**/templates/layouts/*.html'
        ]
    },
    theme: {
        extend: {
            fontWeight: {
                1000: '1000'
            },
            colors: {
                jet: '#2A2B2E',
                'smoky': { 
                    DEFAULT: '#1a140f', 
                    100: '#050403', 
                    200: '#0a0806', 
                    300: '#100c09',
                    400: '#15100c',
                    500: '#1a140f',
                    600: '#554231',
                    700: '#916f53',
                    800: '#ba9f88',
                    900: '#ddcfc3' 
                }, 
                'paprika': { 
                    DEFAULT: '#bb3626',
                    100: '#250b08',
                    200: '#4b150f',
                    300: '#702017',
                    400: '#952a1f',
                    500: '#bb3626',
                    600: '#d85041',
                    700: '#e27c71',
                    800: '#eca8a0',
                    900: '#f5d3d0'
                }, 
                'citrine': { 
                    DEFAULT: '#d59827',
                    100: '#2a1e08',
                    200: '#543c0f',
                    300: '#7f5a17',
                    400: '#a9791f',
                    500: '#d59827',
                    600: '#dfac4f',
                    700: '#e7c17b',
                    800: '#efd6a7',
                    900: '#f7ead3'
                }, 
                'jade': { 
                    DEFAULT: '#32a658',
                    100: '#0a2112',
                    200: '#144223',
                    300: '#1e6335',
                    400: '#278446',
                    500: '#32a658',
                    600: '#49c973',
                    700: '#76d696',
                    800: '#a4e4b9',
                    900: '#d1f1dc'
                }, 
                'eminence': { 
                    DEFAULT: '#782a7e',
                    100: '#180819',
                    200: '#301132',
                    300: '#48194c',
                    400: '#602265',
                    500: '#782a7e',
                    600: '#aa3bb1',
                    700: '#c565cc',
                    800: '#d898dd',
                    900: '#ecccee' },
                'twilight': {
                    DEFAULT: '#2a4e8c',
                    100: '#08101c',
                    200: '#111f39',
                    300: '#192f55',
                    400: '#223f71',
                    500: '#2a4e8c',
                    600: '#396bc0',
                    700: '#688fd2',
                    800: '#9ab4e1',
                    900: '#cddaf0' 
                }
            },
            fontFamily: {
                sans: ['Inter', 'sans-serif'],
                heading: ['DM Sans', 'Inter', 'sans-serif']
            }
        },
    }
};