import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { map } from 'rxjs/operators';

const httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};

@Injectable({
  providedIn: 'root',
})
export class GraphService {
     constructor(private http: HttpClient) {}

    // Uses http.get() to load data from a single API endpoint
    getDonorByState() {
        return this.http.get('http://localhost:3000/api/users&state/').pipe(map(res => console.log(res)));
    }

}
