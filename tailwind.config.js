module.exports = {
    purge: [],
    darkMode: false, // or 'media' or 'class'
    theme: {
        extend: {
            spacing: {
                // 왼쪽은 classname을 위해서 사용, 오른쪽은 css를 위해서 사용
                "25vh": "25vh",
                "50vh": "50vh",
                "60vh": "60vh",
                "65vh": "65vh",
                "70vh": "70vh",
                "75vh": "75vh",
                "80vh": "80vh",
                "90vh": "90vh",
                "95vh": "95vh",
                "100vh": "100vh",
                "103vh": "103vh",
                "105vh": "105vh",
                "110vh": "110vh",
            },
            borderRadius: {
                xl: "1.5rem"
            },
            boxShadow: {
                "wan": "0px 2px 10px 2px rgba(189, 195, 204, 0.20);",
            },
        },
    },
    variants: {
        extend: {},
    },
    plugins: [],
}
