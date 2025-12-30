import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Product {
  iid: number;
  iname: string;
  icategory: string;
  price: number;
  quantity: number;
}

@Injectable({
  providedIn: 'root'
})
export class ProductService {
  private apiUrl = 'http://127.0.0.1:8000/products/';

  constructor(private http: HttpClient) {}

  getProducts(): Observable<Product[]> {
    return this.http.get<Product[]>(this.apiUrl);
  }

  addProduct(product: Product): Observable<any> {
    return this.http.post(this.apiUrl, product);
  }

  updateProduct(iid: number, product: Product): Observable<any> {
    return this.http.put(`${this.apiUrl}${iid}`, product);
  }

  deleteProduct(iid: number): Observable<any> {
    return this.http.delete(`${this.apiUrl}${iid}`);
  }
}
