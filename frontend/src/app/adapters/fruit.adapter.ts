import { Fruit } from "app/types"

export const fruitAdapter = (fruitData: any): Fruit => {
    return {
        id: fruitData.id,
        name: fruitData.name,
        price: fruitData.price,
        category: fruitData.category

    }
} 