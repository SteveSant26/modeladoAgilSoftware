import { Category } from "app/types"

export const categoryAdapter = (fruitData: any): Category => {
    return {
        id: fruitData.id,
        name: fruitData.name,

    }
} 