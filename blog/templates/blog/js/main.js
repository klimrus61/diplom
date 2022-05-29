"use strict"
// alert('Вы');
/*
let browser = prompt('Введите значение браузера', '');
if (browser == 'Edge') {
  alert("You've got the Edge!");
}
else if (browser == 'Chrome' || browser == 'Firefox' || browser == 'Safari' || browser == 'Opera') {
  alert('Okay we support these browsers too');
}
else {
      alert( 'We hope that this page looks ok!' );
}*/



/*
let browser = prompt('input browser', '');
switch (browser) {
  case 'Edge':
  alert('edge');
  break;

  case 'Opera':
  case 'Firefox':
  case 'Safari':
  case 'Chrome':
  alert ('Opera, F, G, C');
  break;

  default:
  alert('we hope');
  break;
}*/


/*

const number = +prompt('Введите число между 0 и 3', '');

if (number === 0) {
  alert('Вы ввели число 0');
}

if (number === 1) {
  alert('Вы ввели число 1');
}

if (number === 2 || number === 3) {
  alert('Вы ввели число 2, а может и 3');
}
*/

/*const number = +prompt('Input value between 0 and 3', ' ');
switch (number) {

  case 0:
  alert('input 0');
  break;

  case 1:
  alert('input 1');
  break;

  case 2:
  case 3:
  alert('input 1 or 2');
  break;

  default:
  alert('erorr');
}
*/


/*function checkAge(age) {
  if (age > 18) {
    return true;
  } else {
    return confirm('Родители разрешили?');
  }
}
*/


/*let a = prompt('input a');
let b = prompt('input b');
function Min(a, b) {
  if (a < b) {
    return a;
  } else {
    return b;
  }
}
alert (Min(a, b));*/




/*let x = prompt('input x');
let y = prompt('input y');
*/
/*function pow(x, y) {
  let result = x;

  for ( let i = 1; i < y; i++) {
    result *= x;
  }

  return result;
}

let x = prompt('input x');
let y = prompt('input y');

  if (y < 0) {
    alert('no ');
  } else {
    alert ( pow(x, y) );
  }


*/


/*function pow(x, y) {
  if (y <= 0) {
    return false;
  } else {
    return (x ** y);
  }
}
alert (pow(x, y));*/


/*
function ask(question, yes, no) {
  if (confirm(question)) yes()
  else no();
}

ask(
  "Вы согласны?",
  () => alert("Вы согласились."),
  () => alert("Вы отменили выполнение.")
);
*/
/*let user = {
  name: "John",
  age: 30
};

let key = prompt("Что вы хотите узнать о пользователе?", "name");

// доступ к свойству через переменную
alert( user[key] ); // John (если ввели "name")
*/
/*
let fruit = prompt("Какой фрукт купить?", "apple");
let bag = {};

// имя свойства будет взято из переменной fruit
bag[fruit] = 5;
alert( bag[fruit] );

*/
/*
let user = {
  name: "John",
  surname: "Smith",
};

user.surname = "QWERTY";
 delete user.name;
 delete user.surname;

console.log(user)
for (let key in user) {
  alert( key );
  alert( user[key] );
}*/
/*
function isEmpty(obj) {
  for (let key in obj) {
    return false;
  }
  return true;
}

let schedule = {};

alert( isEmpty(schedule) ); // true

schedule["8:30"] = "get up";

alert( isEmpty(schedule) ); // false



*/

/*let salaries = {
  John: 100,
  Ann: 160,
  Pete: 130
}
let sum = 0;
  for( let key in salaries) {
    sum += salaries[key];
  }
  alert(sum);
*/



// до вызова функции
/*let menu = {
  width: 200,
  height: 300,
  title: "My menu"
};

function multiplyNumeric(obj)  {
  for (let key in obj) {
    if (typeof obj[key] == 'number') {
      obj[key] *= 2;
    }
  }
}

multiplyNumeric(menu);
console.log(menu);

*/


/*
let calculator = {

  read (a, b) {
    this.first = +prompt('Введите первое число', '');
    this.second = +prompt('Введите второе число', '');
  },

  sum() {
    return this.sum = this.first + this.second;
  },

  mul() {
    return this.mul = this .first * this.second;
  },

};
console.log(this);


calculator.read();
alert( calculator.sum() );
alert( calculator.mul() );
*/
/*
let ladder = {
  step: 0,
  up() {
    this.step++;
    return ladder;
  },
  down() {
    this.step--;
    return ladder;
  },
  showStep: function() { // показывает текущую ступеньку
    alert( this.step );
  }
};

ladder.up().up().up().down();
ladder.showStep();
*/
/*
let obj = {};

function A() {return obj};
function B() {return obj};

let a = new A;
let b = new B;

console.log(new A() == new B());
*/


/*
            function read(prompt('input value', '') {
              return
            }*/



/*
function Calculator() {

  this.read = function() {
    this.first = +prompt('Введите первое число', '');
    this.second = +prompt('Введите второе число', '');
  };
    this.mul = function() {
    return this.first * this.second;
  };
    this.sum = function() {
      return this.first + this.second;
  };
}

let calculator = new Calculator();
calculator.read();

alert( "Sum=" + calculator.sum() );
alert( "Mul=" + calculator.mul() );

*/
/*
function Accumulator(startingValue) {
  this.value = startingValue;

  this.read = function() {
    // this.value = +prompt('Input value', 0);
    this.value += +prompt('Input value', 0);
  };
}

let accumulator = new Accumulator(1);

accumulator.read();
accumulator.read();

alert(accumulator.value);

console.log(accumulator);
*/

/*let obj = {
name: 'Имя',
year: 1986,
toString() { return this.name;},
valueOf() { return this.year}
};
alert( obj ); // Имя, при обращении как к тексту
alert( +obj ); // 1986, при обращении как к числу
*/

// alert( 999999999999999999 );

/*let user = {};
user.name = "John";
user.surname = "Smith";

user.name = "Pete";
delete user.surname;

console.log(user);
*/

/*isEmpty(obj) {
  for (let key in obj) {
    alert()
  };
}*/

/*let user = {
  name: "Иван",
  age: 30
};

let clone = Object.assign({}, user);
console.log(clone);


let ab = {};*/

/*function Calculator() {

  this.read = function() {
    this.first = +prompt('input value 1', '');
    this.second = +prompt('input value 2', '');
  };

  this.sum = function() {
    return this.first + this.second;
  };

  this.mul = function() {
    return this.first * this.second;
  };
}

let calculator = new Calculator();
calculator.read();

alert( "Sum=" + calculator.sum() );
alert( "Mul=" + calculator.mul() );*/
/*
function Accumulator(startingValue) {
  this.value = startingValue;

  this.read = function() {
    this.value += +prompt('новое значение', '');
  };
}

let accumulator = new Accumulator(1); // начальное значение 1

accumulator.read(); // прибавит ввод prompt к текущему значению
accumulator.read(); // прибавит ввод prompt к текущему значению

alert(accumulator.value); // выведет сумму этих значений
*/

/*
let readNumber = function() {
let a = prompt('input VALUE', '');
  if (a == Number) {
    return +a;
 }
  else if (a != Number || a == null) {
    return null;
 }
  else {
    let a = prompt('input VALUE', '');
  }
  alert(+a);
};

readNumber();
*/




































































