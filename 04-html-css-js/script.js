
// prevent sending ambiguous data
document.getElementById('asap').addEventListener("click", (e) => {
  if (e.target.checked) {
    document.getElementById('time').disabled = true;
    document.getElementById('time').style.opacity = 0;
    document.getElementById('or').style.opacity = 0;

    document.getElementById('asap').required = true;
  } else {
    document.getElementById('time').disabled = false;
    document.getElementById('time').style.opacity = 1;
    document.getElementById('or').style.opacity = 1;
  }

  document.getElementById('time').required = false;
})
document.getElementById('time').addEventListener("change", (e) => {
  if (e.target.value) {
    document.getElementById('time').required = true;
    document.getElementById('asap').required = false;
  }
})


// collect order to cart by "add to cart" button
// get a string with order content
// create cart storage controllable from page

var cart;
var cartHtmlContainer = document.querySelector('div.order-content');
makePizzaObjFromOrderPanel = () => {
  pizzaTypeArr = [...document.querySelectorAll('input[name="pizza_type"]:checked')];
  pizzaType = pizzaTypeArr.length ? pizzaTypeArr[0].value : "";
  if (pizzaType == "") {return}
  pizzaSizeArr = [...document.querySelectorAll('input[name="pizza_size"]:checked')];
  pizzaSize = pizzaSizeArr.length ? pizzaSizeArr[0].value : "";
  if (pizzaSize == "") {return}
  toppings_els = [...document.querySelectorAll('input[type="checkbox"][name="topping"]:checked')];
  toppings_values = [];
  toppings_els.forEach((topping) => {
    toppings_values.push(topping.value)
  })

  return {
    type: pizzaType,
    size: pizzaSize,
    toppings: toppings_values
  }
}

addPizzaToCart = (pizzaObj) => {
  if (!cart || cart === undefined) {cart = {}}
  if (!pizzaObj) {return}
  newPizza = new PizzaItem(pizzaObj, cart);
  newPizza.makeDOMElement();
  newPizza.addEventListenerToRemoveButton();
}

drawUpCartAsString = () => {
  let cart_str = '';
  if (!cart || cart === undefined) {return ''}
  let keys = Object.keys(cart);
  if (!keys.length) {return ''}
  keys.forEach((id, index, arr) => {
    cart_str += cart[id].makeGETReqStr();
    if ( !(index+1 == arr.length) ) {
      cart_str += ",";
    }
  })
  return cart_str
}

class PizzaItem {
  constructor(obj, cart) {
    this.id = Date.now();
    this.obj = obj;
    this.cart = cart;
    this.cart[this.id] = this;
  }

  makeDOMElement() {
    let  humanReadableStr = this.makeHumanReadableStr()
    cartHtmlContainer.innerHTML += 
    `
      <div class="pizza-item" id="${this.id}">
        <span class="pizza-str">
          ${humanReadableStr}
        </span>
        <span class="remove-pizza-item-button"></span>
      </div>
    `;
    return document.getElementById(this.id);
  }

  addEventListenerToRemoveButton = () => {
    // for some unknown reason only the last element was getting the event listener, so... :
    Object.keys(this.cart).forEach((id) => {
      document.getElementById(id).
      querySelector('.remove-pizza-item-button').
        addEventListener('click', (e) => {
          const id = e.target.parentElement.id;
          const pizzaItem = this.cart[id];
          pizzaItem.delete();
        });
    })
    document.getElementById(this.id).
    querySelector('.remove-pizza-item-button').
      addEventListener('click', (e) => {
        const id = e.target.parentElement.id;
        if ( this.cart[id] === undefined ) { return }
        const pizzaItem = this.cart[id];
        pizzaItem.delete();
      });
  }

  delete() {
    document.getElementById(this.id).remove();
    delete cart[this.id];
  }

  makeGETReqStr = () => {
    let str = "";
    str += this.obj.type;
    str += "_" + this.obj.size
    if (this.obj.toppings.length) {
      str += "_";
      this.obj.toppings.forEach((topping, index, arr) => {
        if ( index != 0 ) {
          str += "_"
        }
          str += topping
          
      })
    }
  
    return str;
  }
  
  makeHumanReadableStr = () => {
    let str = "";
    str += this.obj.type;
    str += " " + this.obj.size
    if (this.obj.toppings.length) {
      str += " (";
      this.obj.toppings.forEach((topping) => {
        str += "+" + topping
      })
      str += ")";
    }
  
    return str;
  }
}

document.getElementById("addToCart").addEventListener('click', (e) => {
  e.preventDefault();
  addPizzaToCart(makePizzaObjFromOrderPanel());
})


document
  .querySelector('input[type="submit"][value="make an order"]')
    .addEventListener('click', () => {
  // satisfy requirement about data in GET request +
  

  document.getElementById("fake_order_content").innerHTML = drawUpCartAsString();
  order_content = document.querySelector('div.order-content');
  order_content_fake_input = document.getElementById("fake_order_content");
  
  // behavior for "required" asterisks
  order_content_fake_input.invalid = order_content.innerHTML == '' ? 1 : 0;

  document.querySelector('.required-asterisk[for="name"]').style.opacity = 
    document.querySelector('input[name="name"]').invalid ||
      document.querySelector('input[name="name"]:invalid') ? 1 : 0;

  document.querySelector('.required-asterisk[for="phone"]').style.opacity = 
    document.querySelector('input[name="phone"]').invalid ||
      document.querySelector('input[name="phone"]:invalid') ? 1 : 0;

  document.querySelector('.required-asterisk[for="adress"]').style.opacity =
    document.querySelector('input[name="adress"]').invalid ||
      document.querySelector('input[name="adress"]:invalid') ? 1: 0;

  document.querySelector('.required-asterisk[for="order_content"]').style.opacity =
    document.querySelector('textarea[name="order_content"]').invalid ||
      document.querySelector('textarea[name="order_content"]:invalid') ? 1 : 0;

  document.querySelector('.required-asterisk[for="time"]').style.opacity =
    document.querySelector('select[name="time"]').invalid ||
      document.querySelector('select[name="time"]:invalid') ? 1 : 0;

  document.querySelector('.required-asterisk[for="payment"]').style.opacity =
    document.querySelector('input[name="payment"]').invalid ||
      document.querySelector('input[name="payment"]:invalid') ? 1 : 0;
});

// prevent sending extra data from inputs
// for pizza parameters by disabling extra inputs
document.querySelector('form.form-container')
  .addEventListener("submit", () => {
  [...document.
    querySelectorAll('[name="pizza_type"],[name="pizza_size"],[name="topping"]')]
      .forEach((input) => {
    input.disabled = true;
  })
})
// enable inputs again on each load of page
window.onload = () => {
  [...document.
    querySelectorAll('[name="pizza_type"],[name="pizza_size"],[name="topping"]')]
      .forEach((input) => {
    input.disabled = false;
  })
}
