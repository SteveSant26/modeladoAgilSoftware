import { Fruit } from "app/types"
import { fruitAdapter } from "./fruit.adapter"

export const fruitsAdapter = (fruitData: any): Fruit[] => {
    if (Array.isArray(fruitData)) {
        return fruitData.map(fruitAdapter)
    }

    if (Array.isArray(fruitData?.fruits)) {
        return fruitData.fruits.map(fruitAdapter)
    }

    console.warn("Unexpected fruit data format:", fruitData)
    return []
} 