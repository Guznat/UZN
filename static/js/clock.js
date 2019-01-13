function clock() {
        var time = new Date();

        var godzina = time.getHours();
        if (godzina < 10) godzina = "0" + godzina;

        var minuta = time.getMinutes();
        if (minuta < 10) minuta = "0" + minuta;

        var sekunda = time.getSeconds();
        if (sekunda < 10) sekunda = "0" + sekunda;

        document.getElementById("zegar").innerHTML =
              godzina + ":" + minuta + ":" + sekunda;
        setTimeout("clock()", 1000);
    }
clock();
