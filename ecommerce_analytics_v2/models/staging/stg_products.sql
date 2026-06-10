with source as (
    select * from {{source('ecommerce_v2','raw_products')}}
),
renamed as (
        select
            id as product_id,
            title as product_name,
            price as product_price,
            category as product_category,
            description as product_description,
            rating_rate as rating,
            rating_count as review_count
        from source
)
select * from renamed