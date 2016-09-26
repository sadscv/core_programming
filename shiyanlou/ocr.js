var ocrDemo = {
    CANVAS_WIDTH: 200,
    TRANSLATED_WIDTH: 20,
    PIXEL_WIDTH: 10,
    BATCH_SIZE: 1,

    //Server Variables
    PORT: "8000",
    HOST: "http://127.0.0.1",

    //Color Variables
    BLACK: "#000",
    BLUE: "#00f",

    //  client training set
    trainArray: [],
    trainingRequestCount: 0,

    onLoadFunction: function(){
        this.resetCanvas();
    },


    resetCanvas: function() {
        var canvas = document.getElementById('canvas');
        var ctx = canvas.getContext('2d');

    }








}