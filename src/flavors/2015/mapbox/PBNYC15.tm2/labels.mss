// Country labels //
#country_label[zoom>=3] {
  text-name: @name;
  text-face-name: @sans_bold;
  text-fill: @text;
  text-size: 12;
  text-halo-fill: @land;
  text-halo-radius: 1;
  text-wrap-width: 50;
  [zoom>=3][scalerank=1],
  [zoom>=4][scalerank=2],
  [zoom>=5][scalerank=3],
  [zoom>=6][scalerank>3] {
    text-size: 14;
  }
  [zoom>=4][scalerank=1],
  [zoom>=5][scalerank=2],
  [zoom>=6][scalerank=3],
  [zoom>=7][scalerank>3] {
    text-size: 16;
  }
  [zoom>=6][scalerank=1],
  [zoom>=7][scalerank=2],
  [zoom>=8][scalerank>=3] {
    text-size: 20;
  }
}

#country_label_line { 
  line-color: @text;
  line-dasharray: 3,3;
  line-width: 1;
}

// Council district labels //
#districts::labels[zoom>12] { 
  text-face-name: @sans;
  text-name: 'District ' + [CounDist];
  text-fill: #00f;
  text-halo-fill: @land;
  text-halo-radius: 2;
  text-placement: line;
  text-placement-type: simple;
  text-vertical-alignment: top;
  text-margin: 100;
  text-dy: -5;
  //text-spacing: 500;
  text-clip: true;
  
  text-avoid-edges: true;
  text-allow-overlap: false;
  
  [zoom=13] {
    text-size: 10;
    text-dy: -8;
  }
  
  [zoom>14] {
    text-size: 12;
  }
}

// State labels //
#state_label { 
  text-name: @name;
  text-face-name: @sans;
  text-fill: @text;
  text-size: 12;
  text-halo-fill: @land;
  text-halo-radius: 1;
  text-wrap-width: 50;
}

// Display capital cities alongside stars.
#place_label::capitals[type='city'][capital=2][zoom<9] { 
  shield-file: url("star.svg");
  shield-name: @name;
  shield-face-name: @sans;
  shield-size: 14;
  shield-fill: @text;
  shield-halo-fill: @land;
  shield-halo-radius: 1;
  shield-unlock-image: true;
  shield-wrap-width: 80;
  shield-line-spacing: -2;
  // Fine-tune label positioning.
  [ldir='E'] { shield-text-dx: 6; }
  [ldir='W'] { shield-text-dx: -6; }
  [ldir='N'] { shield-text-dy: -5; }
  [ldir='S'] { shield-text-dy: 6; }
  [ldir='NE'] { shield-text-dx: 3; shield-text-dy: -3; }
  [ldir='SE'] { shield-text-dx: 3; shield-text-dy: 3; }
  [ldir='SW'] { shield-text-dx: -3; shield-text-dy: 3; }
  [ldir='NW'] { shield-text-dx: -3; shield-text-dy: -3; }

  [zoom>=6] { shield-size: 16; } 
}

// Display low zoom cities alongside points.
#place_label[type='city'][localrank=1][zoom>=4][zoom<9],
#place_label[type='city'][localrank=2][zoom>=5][zoom<10],
#place_label[type='city'][localrank=3][zoom>=7][zoom<10],
#place_label[type='city'][localrank>=4][localrank>9][zoom>=8][zoom<10],
#place_label[type='town'][localrank<=1][zoom>=9][zoom<10] {
  shield-name: @name;
  shield-face-name: @sans;
  shield-size: 12;
  shield-fill: @text;
  shield-halo-fill: @land;
  shield-halo-radius: 1;
  shield-unlock-image: true;
  shield-file: url("dot.svg");
  shield-wrap-width: 80;
  shield-line-spacing: -2;

  // Fine-tune label positioning.
  [ldir='E'] { shield-text-dx: 6; }
  [ldir='W'] { shield-text-dx: -6; }
  [ldir='N'] { shield-text-dy: -5; }
  [ldir='S'] { shield-text-dy: 6; }
  [ldir='NE'] { shield-text-dx: 3; shield-text-dy: -3; }
  [ldir='SE'] { shield-text-dx: 3; shield-text-dy: 3; }
  [ldir='SW'] { shield-text-dx: -3; shield-text-dy: 3; }
  [ldir='NW'] { shield-text-dx: -3; shield-text-dy: -3; }

  [zoom>=6] { shield-size: 14; }

  // Emphasize major cities.
  [scalerank<=6] { shield-size: 14; }
  [zoom>=6][scalerank<=6] { shield-size: 16; } 
}

// Gradually replace shields with regular text labels.
#place_label[type='city'][localrank=1][zoom>=9],
#place_label[type='city'][zoom>=10] {
  text-name: @name;
  text-face-name: @sans;
  text-size: 16;
  text-fill: @text;
  text-halo-fill: @land;
  text-halo-radius: 1;
  text-min-distance: 4;
  text-wrap-width: 80;
  [scalerank<=3] { 
    text-fill: @text;
    text-size: 20;
  } 
}

// Mid priority place labels //
#place_label[type='town'][localrank<=2][zoom>=10],
#place_label[type='village'][localrank<=2][zoom>=12],
#place_label[type='hamlet'][localrank<=2][zoom>=13],
#place_label[type='town'][zoom>=14],
#place_label[type='village'][zoom>=14],
#place_label[type='hamlet'][zoom>=14] { 
  text-name: @name;
  text-face-name: @sans;
  text-size: 14;
  text-fill: @text;
  text-halo-fill: @land;
  text-halo-radius: 2;
  text-min-distance: 4;
  text-wrap-width: 80;
  [zoom>=12] { 
    text-size: 16;
    text-fill: @text;
  }
}

// Low priority place labels //
#place_label[type='suburb'][localrank<=2][zoom>=12],
#place_label[type='neighbourhood'][localrank<=2][zoom>=13],
#place_label[type='suburb'][zoom>=14],
#place_label[type='neighbourhood'][zoom>=15] { 
  text-name: @name;
  text-face-name: @sans;
  text-size: 14;
  text-fill: @text;
  text-halo-fill: @land;
  text-halo-radius: 2;
  text-min-distance: 4;
  text-wrap-width: 60;
}

// Road labels
#road_label[len>2000][zoom>=12],
#road_label[len>1000][zoom>=15] { 
  text-placement: line;
  text-transform: uppercase;
  text-face-name: @sans;
  text-name: @name;
  text-size: 9;
  //text-min-distance: 100;
  text-halo-fill: @land;
  text-halo-radius: 1;
  text-fill: @text;
  text-margin: 10;
  [zoom>=17] { text-size: 11;}
}

#school-points {
  marker-line-color: @land;
  marker-line-opacity: 0;
  marker-fill: @pbred;
  marker-fill-opacity: 0.3;
  marker-width: 1;
  marker-height: 1;

  [zoom>=11] {
    marker-width: 2;
    marker-height: 2;
  }
  
  [zoom>=12] {
    marker-width: 3;
    marker-height: 3;
  }
  
  [zoom>=13] {
    marker-line-opacity: 1;
    marker-fill-opacity: 0.5;
  }
  
  [zoom>=14] {
    marker-file: url("gradcap-red.png");
    marker-width: 10;
    marker-height: 10;
  }
  
  [zoom>=15] {
    marker-width: 12;
    marker-height: 12;
    
    text-transform: capitalize;
    text-face-name: @sans;
    text-name: [FacName];
    text-size: 9;
    //text-min-distance: 100;
    text-halo-fill: @land;
    text-halo-radius: 1;
    text-fill: @pbred;
    text-wrap-width: 50;
    text-dy: 11;
    text-margin: 2;
  }
  
  [zoom>=16] {
    marker-width: 16;
    marker-height: 16;
  }
  
  [zoom>=17] {
    text-size: 11;
  }
}

#subway-stops[zoom>=14] {
//  marker-line-color: @land;
//  marker-fill: @text;
  marker-file: url("icon_train-blue.png");
  marker-width: 8;
  marker-height: 8;
  
  [zoom>=16] {
    marker-width: 12;
    marker-height: 12;
    
    text-transform: capitalize;
    text-face-name: @sans;
    text-name: [STOP_NAME];
    text-size: 9;
    //text-min-distance: 100;
    text-halo-fill: @land;
    text-halo-radius: 1;
    text-fill: @pblightblue;
    text-wrap-width: 50;
    text-dy: 11;
  }
  
  [zoom>=17] {
    text-size: 11;
  }
}

#nycha-development-points {
  [zoom>=14] {
    text-transform: capitalize;
    text-face-name: @sans;
    text-name: [DEVELOPMEN] + " Housing Development";
    text-size: 9;
    //text-min-distance: 100;
    text-halo-fill: @land;
    text-halo-radius: 1;
    text-fill: @pborange;
    text-wrap-width: 50;
    text-dy: 11;
  }

  [zoom>=15] { text-size: 11;}
  [zoom>=17] { text-size: 13;}
}

// Water labels
#marine_label { 
  text-name: @name;
  text-face-name: @sans_bold;
  text-fill: @text;
  text-size: 12;
  text-halo-fill: @water;
  text-halo-radius: 1;
  text-wrap-before: true;
  text-wrap-width: 90;
  [labelrank=1] {
   text-size: 18;
  }
}

#water_label {
  [zoom<=13],
  [zoom>=14][area>500000],
  [zoom>=16][area>10000],
  [zoom>=17] {
    text-name: @name;
    text-face-name: @sans_bold;
    text-fill: @text;
    text-size: 12;
    text-halo-fill: @water;
    text-halo-radius: 1;
    text-wrap-width: 60;
    text-wrap-before: true;
    text-avoid-edges: true;
  }
}

#waterway_label[type='river'][zoom>=13],
#waterway_label[type='canal'][zoom>=14],
#waterway_label[type='stream'][zoom>=15] { 
  text-name: @name;
  text-face-name: @sans_bold;
  text-fill: @text;
  text-min-distance: 60;
  text-size: 10;
  text-halo-fill: @water;
  text-halo-radius: 1;
  text-wrap-before: true;
  text-avoid-edges: true;
  text-placement: line;
}

// Place labels
#poi_label[maki='park'][scalerank<=2],
#poi_label[maki='airport'][scalerank<=2],
#poi_label[maki='airfield'][scalerank<=2],
#poi_label[maki='rail'][scalerank<=2],
#poi_label[maki='school'][scalerank<=2],
#poi_label[scalerank='hospital'][scalerank<=2] { 
  text-face-name: @sans_bold;
  text-allow-overlap: false;
  text-name: @name;
  text-size: 9;
  text-line-spacing: -2;
  text-min-distance: 50;
  text-wrap-width: 60;
  text-halo-fill: @land;
  text-halo-radius: 1;
  text-fill: @text;
}
