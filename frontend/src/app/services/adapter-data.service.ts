import { HttpClient } from '@angular/common/http';
import { inject, Injectable } from '@angular/core';
import { environment } from '@Enviroments/enviroment';
import { catchError, map, throwError } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AdapterDataService {
  private http = inject(HttpClient);
  private baseUrl = environment.apiUrl;

  getAdaptedData<T>(url: string, adapter: (data: any) => T) {
    return this.http.get<T>(this.baseUrl + url).pipe(
      map((data) => {

        return adapter(data)

      }),
      catchError((err) => throwError(() => err))
    );
  }

  postData<T>(url: string, data: any, adapter: (data: any) => T) {
    return this.http.post(this.baseUrl + url, data).pipe(
      map((data) => {
        return adapter(data);
      }),
      catchError((err) => throwError(() => err)))
  }

  updateData<T>(url: string, data: any, adapter: (data: any) => T) {
    return this.http.put(this.baseUrl + url, data).pipe(
      map((data) => {
        return adapter(data)
      }),
      catchError((err) => throwError(() => err)))
  }
  deleteData<T>(url: string, adapter: (data: any) => T) {
    return this.http.delete(this.baseUrl + url).pipe(
      map((data) => {
        return adapter(data)
      }),
      catchError((err) => throwError(() => err)))
  }



}