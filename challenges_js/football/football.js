var fs = require("fs");

fs.readFileSync(process.argv[2]).toString().trim().split('\n').forEach(function(line) {
  var teams = {};
  var output = "";

  line.split("|").forEach(function(l, i) {
    var countryTeams = l.trim().split(" ");
    countryTeams.forEach(function(team) {
      if (teams.hasOwnProperty(team)) {
        teams[team].push(i+1);
      } else {
        teams[team] = [i+1];
      }
    });
  });

  Object.keys(teams).forEach(function(key) {
    output += key + ":" + teams[key].join(",") + "; ";
  });

  console.log(output);
});
