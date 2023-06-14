import { Component } from '@angular/core';
import { NewUser } from '../newuser';
import { CommunicationsService } from '../communications.service';
import { USERS } from 'mock-users';
import { HttpClientModule } from '@angular/common/http';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-forgot-password',
  templateUrl: 'forgot-password.component.html',
  styleUrls: ['forgot-password.component.css']
})
export class ForgotPasswordComponent {
  constructor(private communicationsService: CommunicationsService, private http: HttpClient) {

  }

  sendData(): void {
    const body = {
      "ts": 1666818622000,
      "cId": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
      "p": {
        "username": "DoeJ1970",
        "email": "example@mail.net",
        "phone": 12345678901
      }
    }
    



    const headers = { 'Content-Type': 'application/json' };
    const users = this.http.post('/fb/auth/exchange', body, { headers }).subscribe((response) => {
      console.log(response);
      console.log(body);
    }, (error) => {
      console.error(error)
    });
  }
}
