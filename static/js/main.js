        const ambient = document.getElementById('ambient_auido');
        const bell = document.getElementById('caw_audio');

        // Wait for user interaction to comply with browser autoplay policies
        document.body.addEventListener('click', () => {
            ambient.play();
        }, { once: true });

        // Play bell every 30 seconds
        setInterval(() => {
            bell.play();
        }, 35000);