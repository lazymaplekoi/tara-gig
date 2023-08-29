const flyoutMenu = $('#flyout-menu');
const menuButton = $('#menu-button'); // Add an appropriate trigger element

menuButton.on('click', (e) => {
    console.log('sup!');
    // flyoutMenu.animate({
    //     opacity: 'toggle',
    //     width: 'toggle',
    //     right: 'toggle'
    //   }, {
    //     duration: 800 
    //   });
    flyoutMenu.toggleClass('hide');
});

$('.close-button').on('click', (e) => {
    console.log('brother!');
    flyoutMenu.toggleClass('hide');
});