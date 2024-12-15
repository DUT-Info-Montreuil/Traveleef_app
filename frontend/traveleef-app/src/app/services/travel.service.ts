import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class TravelService {

  private apiUrl = 'http://localhost:5000/travel';

  constructor(private httpClient: HttpClient) { }

  searchFlights(searchData: any): Observable<any> {
    return this.httpClient.post<any>(`${this.apiUrl}/search`, searchData);
  }
}