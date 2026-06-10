with products as (
    select * from {{ref('stg_products')}}
),
users as (
    select * from {{ref('stg_users')}}
),
carts as (
    select * from {{ref('stg_carts')}}
),
finally as (
    select
    u.user_id,
    u.first_name || ' ' || u.last_name as full_name,
    u.user_email,
    sum(c.quantity * p.product_price) as total_lifetime_spend
    from users u join carts c
    on c.user_id = u.user_id
    join products p
    on p.product_id = c.product_id
    group by u.username,u.user_id,u.first_name,u.last_name,u.user_email
)
select * from finally