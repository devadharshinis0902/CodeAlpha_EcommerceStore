/* Vanilla JS Shopping Cart Engine with LocalStorage Persistence */

const CART_KEY = 'codealpha_ecommerce_cart';

/**
 * Get Cart Items from LocalStorage
 */
function getCart() {
    try {
        const data = localStorage.getItem(CART_KEY);
        return data ? JSON.parse(data) : [];
    } catch (e) {
        console.error("Error reading cart from localStorage", e);
        return [];
    }
}

/**
 * Save Cart Items to LocalStorage & Update Badge Counter
 */
function saveCart(cart) {
    try {
        localStorage.setItem(CART_KEY, JSON.stringify(cart));
    } catch (e) {
        console.error("Error saving cart to localStorage", e);
    }
    updateCartBadge();
}

/**
 * Update Header Cart Count Badge
 */
function updateCartBadge() {
    const cart = getCart();
    const totalCount = cart.reduce((sum, item) => sum + item.quantity, 0);
    const badgeElements = document.querySelectorAll('.cart-badge');
    badgeElements.forEach(el => {
        el.textContent = totalCount;
    });
}

/**
 * Add Product to Cart with Stock Enforcement
 */
function addToCart(id, name, price, image, stock, quantityToAdd = 1) {
    id = parseInt(id);
    price = parseFloat(price);
    stock = parseInt(stock);
    quantityToAdd = parseInt(quantityToAdd);

    if (isNaN(quantityToAdd) || quantityToAdd <= 0) quantityToAdd = 1;

    let cart = getCart();
    const existingIndex = cart.findIndex(item => item.id === id);

    if (existingIndex > -1) {
        const newQty = cart[existingIndex].quantity + quantityToAdd;
        if (newQty > stock) {
            showToast(`Cannot add more. Max stock available is ${stock}.`, 'warning');
            cart[existingIndex].quantity = stock;
        } else {
            cart[existingIndex].quantity = newQty;
            showToast(`Updated '${name}' quantity in your cart.`, 'success');
        }
    } else {
        if (quantityToAdd > stock) {
            showToast(`Cannot add more. Max stock available is ${stock}.`, 'warning');
            quantityToAdd = stock;
        }
        cart.push({
            id: id,
            name: name,
            price: price,
            image: image,
            stock: stock,
            quantity: quantityToAdd
        });
        showToast(`Added '${name}' to your cart!`, 'success');
    }

    saveCart(cart);
}

/**
 * Update Item Quantity directly from Cart Page
 */
function updateQuantity(id, newQty) {
    id = parseInt(id);
    newQty = parseInt(newQty);

    let cart = getCart();
    const item = cart.find(i => i.id === id);
    if (!item) return;

    if (newQty <= 0) {
        removeFromCart(id);
        return;
    }

    if (newQty > item.stock) {
        showToast(`Only ${item.stock} units of '${item.name}' in stock.`, 'warning');
        item.quantity = item.stock;
    } else {
        item.quantity = newQty;
    }

    saveCart(cart);
    renderCartPage();
}

/**
 * Remove Item from Cart
 */
function removeFromCart(id) {
    id = parseInt(id);
    let cart = getCart();
    const item = cart.find(i => i.id === id);
    cart = cart.filter(i => i.id !== id);
    saveCart(cart);
    if (item) {
        showToast(`Removed '${item.name}' from your cart.`, 'info');
    }
    renderCartPage();
}

/**
 * Clear Cart
 */
function clearCart() {
    localStorage.removeItem(CART_KEY);
    updateCartBadge();
}

/**
 * Render Cart Page Table and Summary
 */
function renderCartPage() {
    const cartContainer = document.getElementById('cart-items-body');
    const emptyState = document.getElementById('cart-empty-state');
    const layout = document.getElementById('cart-full-layout');
    const subtotalEl = document.getElementById('cart-subtotal');
    const grandTotalEl = document.getElementById('cart-grand-total');

    if (!cartContainer) return; // Not on cart page

    const cart = getCart();

    if (cart.length === 0) {
        if (layout) layout.style.display = 'none';
        if (emptyState) emptyState.style.display = 'block';
        return;
    }

    if (layout) layout.style.display = 'grid';
    if (emptyState) emptyState.style.display = 'none';

    cartContainer.innerHTML = '';
    let total = 0;

    cart.forEach(item => {
        const itemSubtotal = item.price * item.quantity;
        total += itemSubtotal;

        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td>
                <div class="cart-item-info">
                    <img src="${item.image}" alt="${item.name}" class="cart-item-img">
                    <div>
                        <div style="font-weight: 700;">${item.name}</div>
                        <div style="font-size: 0.85rem; color: var(--text-muted);">$${item.price.toFixed(2)} each</div>
                    </div>
                </div>
            </td>
            <td>
                <div class="qty-picker" style="margin: 0;">
                    <button class="qty-btn" onclick="updateQuantity(${item.id}, ${item.quantity - 1})">-</button>
                    <input type="number" class="qty-input" value="${item.quantity}" readonly>
                    <button class="qty-btn" onclick="updateQuantity(${item.id}, ${item.quantity + 1})">+</button>
                </div>
                <div style="font-size: 0.75rem; color: var(--text-muted); margin-top: 4px;">Max: ${item.stock}</div>
            </td>
            <td style="font-weight: 700;">$${itemSubtotal.toFixed(2)}</td>
            <td>
                <button class="btn btn-sm btn-danger" onclick="removeFromCart(${item.id})">Remove</button>
            </td>
        `;
        cartContainer.appendChild(tr);
    });

    if (subtotalEl) subtotalEl.textContent = `$${total.toFixed(2)}`;
    if (grandTotalEl) grandTotalEl.textContent = `$${total.toFixed(2)}`;
}

// Initialize Badge on page load
document.addEventListener('DOMContentLoaded', () => {
    updateCartBadge();
    renderCartPage();
});
