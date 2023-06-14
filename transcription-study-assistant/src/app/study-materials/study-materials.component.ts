import { Component } from '@angular/core';
import { AppComponent } from '../app.component';
import { CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';


@Component({
  standalone: true,
  selector: 'app-study-materials',
  templateUrl: './study-materials.component.html',
  styleUrls: ['./study-materials.component.css'],
  schemas: [
    CUSTOM_ELEMENTS_SCHEMA
  ]
})
export class StudyMaterialsComponent {
  
}

