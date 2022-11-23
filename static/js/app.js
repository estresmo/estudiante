// ************************************************
// Shopping Cart API
// ************************************************

const shoppingCart = (function () {
     // =============================
     // Private methods and properties
     // =============================
     let cart = [];

     // Constructor
     function Item(name, price, count, product_id) {
          this.name = name;
          this.price = price;
          this.count = count;
          this.product_id = product_id;
     }

     // Save cart
     function saveCart() {
          sessionStorage.setItem('shoppingCart', JSON.stringify(cart));
     }

     // Load cart
     function loadCart() {
          cart = JSON.parse(sessionStorage.getItem('shoppingCart'));
     }

     if (sessionStorage.getItem("shoppingCart") != null) {
          loadCart();
     }


     // =============================
     // Public methods and properties
     // =============================
     let obj = {};

     // Add to cart
     obj.addItemToCart = function (name, price, count, product_id) {
          for (let item in cart) {
               if (cart[item].name === name) {
                    cart[item].count++;
                    saveCart();
                    return;
               }
          }
          let item = new Item(name, price, count, product_id);
          cart.push(item);
          saveCart();
     }
     // Set count from item
     obj.setCountForItem = function (name, count) {
          for (const i in cart) {
               if (cart[i].name === name) {
                    cart[i].count = count;
                    break;
               }
          }
     };
     // Remove item from cart
     obj.removeItemFromCart = function (name) {
          for (let item in cart) {
               if (cart[item].name === name) {
                    cart[item].count--;
                    if (cart[item].count === 0) {
                         cart.splice(item, 1);
                    }
                    break;
               }
          }
          saveCart();
     }

     // Remove all items from cart
     obj.removeItemFromCartAll = function (name) {
          for (let item in cart) {
              console.log(name)
              console.log(cart[item])
               if (cart[item].name === name) {
                    cart.splice(item, 1);
                    break;
               }
          }
          saveCart();
     }

     // Clear cart
     obj.clearCart = function () {
          cart = [];
          saveCart();
     }

     // Count cart
     obj.totalCount = function () {
          let totalCount = 0;
          for (let item in cart) {
               totalCount += cart[item].count;
          }
          return totalCount;
     }

     // Total cart
     obj.totalCart = function () {
          let totalCart = 0;
          for (let item in cart) {
               totalCart += cart[item].price * cart[item].count;
          }
          return Number(totalCart.toFixed(2));
     }

     // List cart
     obj.listCart = function () {
          let cartCopy = [];
          for (i in cart) {
               item = cart[i];
               itemCopy = {};
               for (p in item) {
                    itemCopy[p] = item[p];

               }
               itemCopy.total = Number(item.price * item.count).toFixed(2);
               cartCopy.push(itemCopy)
          }
          return cartCopy;
     }

     // cart : Array
     // Item : Object/Class
     // addItemToCart : Function
     // removeItemFromCart : Function
     // removeItemFromCartAll : Function
     // clearCart : Function
     // countCart : Function
     // totalCart : Function
     // listCart : Function
     // saveCart : Function
     // loadCart : Function
     return obj;
})();


// *****************************************
// Triggers / Events
// *****************************************
// Add item
$('.add-to-cart').click(function(event) {
  event.preventDefault();
  let name = $(this).data('name');
  let price = Number($(this).data('price'));
  let product_id = $(this).data('productId');
  shoppingCart.addItemToCart(name, price, 1,product_id);
  displayCart();
});

// Clear items
$('.clear-cart').click(function() {
  shoppingCart.clearCart();
  displayCart();
});


function displayCart() {
  let cartArray = shoppingCart.listCart();
  let output = "";
  for(let i in cartArray) {
    output += "<tr>"
      + "<td>" + cartArray[i].name + "</td>"
      + "<td>$ (" + cartArray[i].price + ")</td>"
      + "<td><div class='input-group'>"
      + "<input type='number' min='1' class='item-count form-control' data-name='" + cartArray[i].name + "' value='" + cartArray[i].count + "'>"
      + "</div></td>"
      + "<td><button class='btn delete-item bg-danger' data-name='" + cartArray[i].name + "'>X</button></td>"
      + " = "
      + "<td>$" + cartArray[i].total + "</td>"
      +  "</tr>";
  }
  $('.show-cart').html(output);
  $('.total-cart').html(shoppingCart.totalCart());
  $('.total-count').html(shoppingCart.totalCount());
}

// Delete item button
showCart = $(".show-cart")



showCart.on("click", ".delete-item", function(event) {
  let name = $(this).data('name')
  shoppingCart.removeItemFromCartAll(name);
  displayCart();
})


// -1
showCart.on("click", ".minus-item", function(event) {
  let name = $(this).data('name')
  shoppingCart.removeItemFromCart(name);
  displayCart();
})
// +1
showCart.on("click", ".plus-item", function(event) {
  let name = $(this).data('name')
  shoppingCart.addItemToCart(name);
  displayCart();
})

// Item count input
showCart.on("change", ".item-count", function(event) {
   let name = $(this).data('name');
   let count = Number($(this).val());
  shoppingCart.setCountForItem(name, count);
  displayCart();
});

displayCart();


