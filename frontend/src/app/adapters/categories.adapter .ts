import { Category, Fruit } from "app/types"
import { categoryAdapter } from "./category.adapter"

export const categoriesAdapter = (categoryData: any): Category[] => {
    if (Array.isArray(categoryData)) {
        return categoryData.map(categoryAdapter)
    }

    if (Array.isArray(categoryData?.categories)) {
        return categoryData.categories.map(categoryAdapter)
    }

    console.warn("Unexpected category data format:", categoryData)
    return []
} 