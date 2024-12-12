import { Injectable } from '@angular/core';

import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class ImageService {
  private apiUrl = 'https://api.unsplash.com/search/photos';
  private accessKey = '';

  constructor(private http: HttpClient) { }

  getImage(query: string): Observable<any> {
    const url = `${this.apiUrl}?query=${query}&client_id=${this.accessKey}&page=1&per_page=1`;
    return this.http.get<any>(url);
  }
}
