function pwgen (number) {

  var passVal = '!"#$%&\'()*+,-./0123456789:;=?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
  var rtn_pass = ''
  for (var i = 0; i < number; i++){
    var randomChoice = Math.floor(Math.random() * Math.floor(passVal.length) + 0);
    rtn_pass = rtn_pass + passVal[randomChoice];
  };
  return rtn_pass;
};
