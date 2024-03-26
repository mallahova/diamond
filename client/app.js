function getBathValue() {
   var uiBathrooms = document.getElementsByName("uiBathrooms");
   for (var i in uiBathrooms) {
      if (uiBathrooms[i].checked) {
         return parseInt(i) + 1;
      }
   }
   return -1; // Invalid Value
}

function getBHKValue() {
   var uiBHK = document.getElementsByName("uiBHK");
   for (var i in uiBHK) {
      if (uiBHK[i].checked) {
         return parseInt(i) + 1;
      }
   }
   return -1; // Invalid Value
}

function onClickedEstimatePrice() {
   console.log("Estimate price button clicked");
   var carat = document.getElementById("uiCarat");
   var cut = document.getElementById("uiCut");
   var color = document.getElementById("uiColor");
   var clarity = document.getElementById("uiClarity");
   var table = document.getElementById("uiTable");
   var x = document.getElementById("uiX");
   var y = document.getElementById("uiY");
   var z = document.getElementById("uiZ");
   var depth = document.getElementById("uiDepth");
   var estPrice = document.getElementById("uiEstimatedPrice");
   var url = "/api/predict_price";

   $.post(url, {
      carat: parseFloat(carat.value),
      cut: cut.value,
      color: color.value,
      clarity: clarity.value,
      table: parseFloat(table.value),
      x: parseFloat(x.value),
      y: parseFloat(y.value),
      z: parseFloat(z.value),
      depth: parseFloat(depth.value)
   }, function (data, status) {
      console.log(data.estimated_price);
      estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + "$</h2>";
      console.log(status);
   });
}

function onPageLoad() {
   console.log("document loaded");
   var url = "/api/get_cut_names"; // Use this if you are NOT using nginx which is first 7 tutorials
   $.get(url, function (data, status) {
      if (data) {
         var cut = data.cut;
         var uiCut = document.getElementById("uiCut");
         $('#uiCut').empty();
         for (var i in cut) {
            var opt = new Option(cut[i]);
            $('#uiCut').append(opt);
         }
      }
   });
   var url = "/api/get_color_categories"; // Use this if you are NOT using nginx which is first 7 tutorials
   $.get(url, function (data, status) {
      if (data) {
         var color = data.color;
         var uiColor = document.getElementById("uiColor");
         $('#uiColor').empty();
         for (var i in color) {
            var opt = new Option(color[i]);
            $('#uiColor').append(opt);
         }
      }
   });
   var url = "/api/get_clarity_categories"; // Use this if you are NOT using nginx which is first 7 tutorials
   $.get(url, function (data, status) {
      if (data) {
         var clarity = data.clarity;
         var uiClarity = document.getElementById("uiClarity");
         $('#uiClarity').empty();
         for (var i in clarity) {
            var opt = new Option(clarity[i]);
            $('#uiClarity').append(opt);
         }
      }
   });
}
window.onload = onPageLoad;
